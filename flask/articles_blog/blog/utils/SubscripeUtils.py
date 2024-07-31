from blog import stripe, db
from flask_login import current_user
from flask import session
from blog.controllers.SubscripeController import StripeCustomer
from datetime import datetime
import time
def stripe_subscription_create(customer_id, price_id):
    print("#"*30)
    print(customer_id)
    print(price_id)
    print("#"*30)
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{
            "price": price_id
        }],
        # الاشتراك غير مكتمل حتى يدفع المستخدم
        # اذا م حددناها سيشترك المستخدم بدون دفع
        payment_behavior="default_incomplete",
        # عند نجاح عملة الدفع احفض بخوادم سترايب    
        payment_settings={
            'save_default_payment_method': 'on_subscription'
        },
        # يوسع الاستجابة لتشمل تفاصيل payment_intent الخاصة بأحدث فاتورة. هذا مفيد لعرض حالة الدفع والتعامل مع أي إجراءات ضرورية مثل إعادة توجيه العميل للدفع.
        expand=['latest_invoice.payment_intent'],
    )
    return subscription


def handle_subscripion_db(data_object):
    customer_db = StripeCustomer.query.filter_by(subscription_id=data_object.id).first()
    if customer_db:
        customer_db.amount = data_object['items']['data' ][0]['price']['unit_amount'] / 100
        customer_db.subscription_type = data_object['items']['data'][0]['plan']['interval']
        customer_db. subscription_start = datetime. fromtimestamp(data_object['current_period_start'])
        customer_db.subscription_end = datetime.fromtimestamp(data_object['current_period_end'])
        customer_db.status = data_object.status
        customer_db.subscription_canceled = data_object.cancel_at_period_end
        db.session.commit()
        
def upgrade_details(price_id):
    customer = StripeCustomer.query.filter_by(user_id=current_user.id).first()
    # استرداد قائمة بطرق الدفع المرتبطة بعميل معين
    payment_method = stripe.Customer.list_payment_methods(
        customer.customer_id,
        type = "card"
    )
    last4 = payment_method['data' ][0]['card']['last4']
    exp_month = payment_method['data'][0]['card']['exp_month']
    exp_year = payment_method['data'][0]['card']['exp_year']
    brand = payment_method['data'][0]['card']['brand']#لوغو

    subscription = stripe.Subscription.retrieve(customer.subscription_id)
    session['item_id'] = subscription['items']['data'][0].id
    items = [{
    'id' : session['item_id'], # si_#####
    'price' : price_id,
    }]
    invoice = stripe.Invoice.upcoming(
        customer = customer.customer_id,
        subscription = customer.subscription_id,
        subscription_items = items,
        subscription_proration_date = int(time.time())
    )

    change_value = invoice["amount_due"] / 100
    sub_description = invoice['lines']['data'][-1]['description']
    return {
        "last4":last4,
        "exp_month":exp_month,
        "exp_year":exp_year,
        "brand":brand,
        "change_value":change_value,
        "sub_description": sub_description,
        }
    
    
    
def subscription_modify(price_id, id):
    # تعديل
    stripe.Subscription.modify(
            id,
            payment_behavior='pending_if_incomplete',
            proration_behavior='always_invoice',
            items=[{
            'id': session['item_id'],
            "price" : price_id,
            }]
        )
    
def subscribe_isCanceled(sub_id, is_cancel):
    stripe.Subscription.modify(
        sub_id,
        cancel_at_period_end=is_cancel
    )
    