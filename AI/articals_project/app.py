from flask import Flask, render_template, request
from utils import chatgpt, diffusion, translate_keywords, transcribe_function, modified_gpt
import os
import tempfile
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/langchain-gpt', methods=['POST'])
def langchain_gpt():
    # يأخذ المدخلات من المستخدم ثم يقوم بإرجاع رد تشات جي بي تي بالاستعانة بلانج تشين
    user_input = request.json.get('user_input')
    return modified_gpt(user_input)


@app.route('/transcribe-api', methods=['POST'])
def transcribe_api():
    # نأخذ الملف المرفوع ونستخرج اسمه ونوعه
    uploaded_file = request.files['file']
    original_filename = uploaded_file.filename
    _, file_extension = os.path.splitext(original_filename)
    # نفتح ملف مؤقت بنفس صيغة الملف المرفوع ونحتفظ به محليا من أجل تفريغه
    with tempfile.NamedTemporaryFile(suffix=file_extension, delete=False) as temp_file:
        temp_path = temp_file.name
        uploaded_file.save(temp_path)
        transcription = transcribe_function(temp_path)
        temp_file.close()
    os.remove(temp_path)
    return transcription

@app.route('/sd-api', methods=['POST'])
def sd_api():
    # نأخذ الوصف للصورة من الطلب ثم نقوم بإدخاله إلى الدالة التي ستقوم بإرجاع صورة من النموذج
    prompt = request.json.get('prompt')
    return {
        'imageUrl': "data:image/png;base64, " + diffusion(translate_keywords(prompt))
    }
    
@app.route('/gpt-api', methods=['POST'])
def gpt_api():
    # يأخذ 3 معاملات، وهما رسالة النظام ومدخلات المستخدم وإن كان الطلب يريد تقسيم المدخلات، ثم يقوم بإرجاع الرد
    system_settings = request.json.get('system_settings')
    user_input = request.json.get('user_input')
    chunk = request.json.get('chunk')
    return chatgpt(user_input, system_settings, chunk)

@app.route('/create-article')
def create_article():
    return render_template('create-article.html')
    
@app.route('/summarize-article')
def summarize_article():
    return render_template('summarize-article.html')

@app.route('/transcribe')
def transcribe():
    return render_template('transcribe.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == "__main__":
    app.run(debug=True)
