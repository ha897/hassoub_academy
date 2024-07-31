from flask import Blueprint
from blog.controllers.MainController import MainController
from blog.controllers.SubscripeController import SubscripeController

SubscribeRouter = Blueprint("subscribe_controller", __name__)

SubscribeRouter.route("/subscription")(SubscripeController.subscription)
SubscribeRouter.route("/create-subscription", methods=["GET", "POST"])(SubscripeController.subscription_create)
SubscribeRouter.route("/public-key")(SubscripeController.get_publishable_key)
SubscribeRouter.route("/webhook", methods=["POST"])(SubscripeController.webhook_received)
SubscribeRouter.route("/subscription-success", methods=["POST"])(SubscripeController.subscription_success)

SubscribeRouter.route("/upgrade-verifying/<price_id>", methods=["GET"])(SubscripeController.upgrade_verifying)
SubscribeRouter.route("/subscription-upgrade/<price_id>", methods=["GET"])(SubscripeController.subscription_upgrade)


SubscribeRouter.route("/update-payment", methods=["GET"])(SubscripeController.change_payment_method)
SubscribeRouter.route("/create-setup-intent", methods=["POST"])(SubscripeController.create_setup_intent)
SubscribeRouter.route("/subscription_cancel/<is_canceled>", methods=["POST"])(SubscripeController.subscription_cancel)