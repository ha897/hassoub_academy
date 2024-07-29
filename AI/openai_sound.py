import openai
"""
استخراج النصوص من الملف الصوتي
"""
# ادخال مفتاح الاي بي اي
openai.api_key = "sk-proj-optVHEHtKJiOiyQAuMjFT3BlbkFJMZX6f0kuyMcSIihJoVYV"
# استخراج صوت
file = open("audio.mp3", 'rb')
response = openai.Audio.transcribe('whisper-1', file)
# طباعة الرد
print(response['text'])