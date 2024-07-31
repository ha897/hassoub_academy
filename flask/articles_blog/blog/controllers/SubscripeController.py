from blog import cfg, stripe, db
from blog.models.SubscribeModel import StripeCustomer
from flask_login import current_user, login_required
from flask import render_template, flash, redirect, url_for, jsonify, request
from blog.utils.SubscripeUtils import stripe_subscription_create, handle_subscripion_db, upgrade_details,subscription_modify, subscribe_isCanceled
import json
class SubscripeController:
    # يرجع المفتاح العام
    def get_publishable_key():
        return jsonify({"publicKey":cfg.STRIPE_PUBLISHABLE_KEY}) 
    def subscription():
        # المستخدم مجهول (لم يسجل دخول)
        # حول للصفحة الرئيسية صصصصصصصصصصصصصصصصص
        if current_user.is_anonymous:
            return render_template("subscribe/subscription.jinja", prices=cfg.prices, title="اشتراك")
        
        customer = StripeCustomer.query.filter_by(user_id= current_user.id).first()
        if customer and customer.status == "active":
            flash('قمت بالاشتراك مسبقا , اذا كنت ترغب بتغيير الاشتراكاضغط على "ادارة الاشتراك"', "warning")
            return redirect(url_for('auth_controller.user_account'))
        else:
            return render_template("subscribe/subscription.jinja", prices=cfg.prices, title="اشتراك") 
    @login_required    
    def subscription_create():
        # انشاء اشتراك
        # لا يمكن للادمن الاشتراك
        if current_user.is_admin:
            flash("لا يمكن للمدير الاشتراك", "warning")
            return redirect(url_for("main_controller.home"))
        customer = StripeCustomer.query.filter_by(user_id=current_user.id).first()
        if customer and customer.status == "active":
            flash("يمكنك تعديل الاشتراك من صفحتك الشخصية", 'warning')
            return redirect(url_for('main_controller.home'))
        try:
            price_id = request.form.get('priceId')
            if not customer:
                new_customer = stripe.Customer.create(
                    email=current_user.email,
                    name=current_user.username
                )

                print("1")
                subscription = stripe_subscription_create(new_customer.id, price_id)
                customer_db = StripeCustomer(
                    user_id=current_user.id,
                    customer_id=new_customer.id,
                    subscription_id=subscription.id
                )

                db.session.add(customer_db)
                db.session.commit()
            else:
                print("2")
                subscription = stripe_subscription_create(customer.customer_id, price_id)
                customer.subscription_id = subscription.id
                db.session.commit()
                
            sub_description = subscription["latest_invoice"]['lines']['data'][0]['description']
            client_secret = subscription.latest_invoice.payment_intent.client_secret
            
            # latest_invoice = subscription.latest_invoice
            # sub_description = latest_invoice.lines.data[0].description
            # client_secret = latest_invoice.payment_intent.client_secret
            
            return render_template('subscribe/payment.jinja', sub_description=sub_description, client_secret=
            client_secret)
        except :
            flash("حدث خطا, قم بالمحاولة لاحقا", 'danger')
            return redirect(url_for('subscribe_controller.subscription'))

    def webhook_received():
        request_data = json.load(request.data)
        webhook_secret = cfg.STRIPE_WEBHOOK_KEY
        if webhook_secret:
            signature = request.headers.get("stripe-signature")
            try:
                # التاكد من صحة الطلب
                event = stripe.Webhook.construct_event(payload=request.data, sig_header=signature, secret=webhook_secret)
                data = event["data"]
            except Exception as e:
                return e
            event_type = event["type"]
        else:
            data = request_data["data"]
            event_type = request_data["type"]
        data_object = data["object"]
        
        # اذا كان تعديل بيانات
        if event_type == "customer.subscripion.updated":
            handle_subscripion_db(data_object)
            print(f"تم انشائ كائن اشتراك {event.id}")
        elif event_type == "invoice.paid":
            print("دفع العميل مسبقا")
            
        elif event_type == "setup_intent.created":
            print('تم إنشاء كائن SetupIntent')
        elif event_type == 'setup_intent.succeeded':
            print('تم إضافة طريقة دفع جديدة لعمليات الدفع المستقبلية')
        elif event_type == 'payment_method.attached':
            print('تم إضافة طريقة الدفع الجديدة إلى كائن العميل')
            
        return jsonify({"status":"success"})
    
    @login_required
    def subscription_success():
        payment_intent_status = request.args.get('paymentIntentStatus')
        if payment_intent_status is None:
            flash( "يمكنك مشاهدة تفاصيل الاشتراك من صفحتك الشخصية", 'warning')
            return redirect(url_for('auth_controller.user_account'))
        if payment_intent_status == "succeeded":
            return render_template('subscribe/payment_success.jinja', title='تم الاشتراك')
        else:
            flash("حدث خطأ أثناء عملية الدفع تحقق من صفحتك الشخصية", 'warning')
            return redirect(url_for('auth_controller.user_account'))

    @login_required
    def upgrade_verifying(price_id):
        if current_user.is_admin:
            flash("لا يمكن للمدير الاشتراك", 'warning')
            return redirect(url_for('main_controller.home'))
        if current_user.stripe_customers[0].subscription_canceled:
            flash("رقم بتفعيل الاشتراك أولا" ,'warning')
            return redirect(url_for('auth_controller.user_account'))

        try:
            new_details = upgrade_details(price_id)
            return render_template('subscribe/upgrade_subscribe.jinja',
                new_details=new_details, price_id=price_id)
        except:
            flash("حدث خطأ أثناء ترقية الاشتراك", 'warning')
            return redirect(url_for('main_controller.home'))
        
    @login_required
    def subscription_upgrade(price_id):
        if current_user.is_admin:
            flash("لا يمكن للمدير الاشتراك", "warning")
            return redirect(url_for('main_controller.home'))
        customer = StripeCustomer.query.filter_by(user_id= current_user.id).first()
        if customer.subscription_canceled:
            flash( "يجب عليك تفعيل الاشتراك أولا", "warning")
            return redirect(url_for('auth_controller.user_account'))
        try:

            subscription_modify(price_id, customer.subscription_id)
            flash(".تم تغيير الاشتراك بنجاح، شكرا لك", 'success')
            return redirect(url_for('auth_controller.user_account'))
        except:
            flash("حدث خطأ أثناء ترقية الاشتراك", "warning")
            return redirect(url_for("main_controller.home"))
        
    @login_required
    def change_payment_method():
        if current_user.is_admin:
            flash("لا يمكنك الوصول للصفحة المطلوبة", "warning")
            return redirect(url_for('main_controller.home'))
        if current_user.stripe_customers[0].subscription_canceled:
            flash("قم بتفعيل الاشتراك أولا", 'warning')
            return redirect(url_for('auth_controller.user_account'))
        return render_template('subscribe/change_payment_method.jinja')

    def create_setup_intent():
        customer = current_user. stripe_customers[0]
        setup_intent = stripe.SetupIntent.create(customer=customer.customer_id)
        return jsonify(setup_intent)

    @login_required
    def subscription_cancel(is_canceled):
        if current_user.is_admin:
            flash("لا يمكنك الوصول للصفحة المطلوبة", 'warning')
            return redirect(url_for('main_controller.home'))
        try:
            customer = StripeCustomer.query. filter_by(user_id=current_user.id).first()
            if customer.status == "active":
                subscribe_isCanceled(customer.subscription_id, is_canceled)
                if not customer.subscription_canceled:
                    flash(' تم إلغاء اشتراكك بنجاح، ستتمكن من قراءة المقالات حتى انتهاء فترة الاشتراك، حتى تلك الفترة .يمكنك إعادة تفعيل الاشتراك إذا كنت ترغب بذلك',"warning")
                else:
                    flash(".تم إعادة تفعيل الاشتراك، شكرا لك", 'warning')
                    return redirect(url_for('auth_controller.user_account'))
        except :
            flash("حدث خطأ أثناء إلغاء الاشتراك", 'warning')
            return redirect(url_for('main_controller.home'))
