import openai
"""
اجراء محادثة مه شات جي بي تي
"""
# ادخال مفتاح الاي بي اي
openai.api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# 
response = openai.ChatCompletion.create(
                #بما اننا نستخدم شات جي بي تي 3 نستخدم الموديل
                model='gpt-3.5-turbo',
                messages=[{'role':"user", "content":"الرساله الي بترسلها للتشات جي بي تي"}]
            )
# طباعة الرد
print(response["choices"][0]["message"]["content"])
