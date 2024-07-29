import base64
import os
import requests
"""
انشاء صور بالذكاء الاصطناعي باستخدام الاي بي اي
"""
    # النموزج المستخدم(الاصدار)
    # engine_id = "stable-diffusion-v1-6"
    # engine_id = "stable-diffusion-xl-1024-v1-0"
    # engine_id = "stable-diffusion-v1-6"
def create_image_api(engine_id, contant, file_name):

    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    #المفتاح الخاص بنا  
    api_key = 'sk-K5Bx12BXZPkaXfJwSfz8TQMflEdiy2Edw0LcJ3bVLmWUpyls'

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            # نوع البيانات المرسل والمرجع
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            # وصف الصورة المراد تكوينها
            "text_prompts": [
                {
                    "text": contant
                }
            ],
            # معلومات الصورة
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(f"{file_name}.png", "wb") as f:
            # ناخذ الصورة بتمثيل بيس سكستي فور نرجعها للاصل
            f.write(base64.b64decode(image["base64"]))


if not os.path.exists("images"):
    os.mkdir("images")
contents = ["images/v1-6", "images/xl-1024-v1-0"]

for  content in contents:
    create_image_api("stable-diffusion-v1-6","red car", content)