from flask import current_app
from datetime import datetime
# وصول عام لهذا المتغير بكل مكان بالنطبيق
@current_app.context_processor
def inject_now():
    return {"now": datetime.now().year}
