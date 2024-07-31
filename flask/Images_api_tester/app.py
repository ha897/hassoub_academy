from flask import Flask ,render_template, jsonify, request, redirect, send_file
import requests, os
from io import BytesIO
from werkzeug.utils import secure_filename
from actions_file import bp as actionbp
from filters import bp as filterbp

app = Flask(__name__)

#ياخذ الوسائط المفتاحية الممررة
app.config.from_mapping(SECRET_KEY="swewrnthmdnfxfzdxzsdrz@N#JWS<Xjudsdcm")


URL = "https://flask-dljn.onrender.com"
app.config['URL'] = URL

S3_URL = 'https://for-images-python.s3.ap-southeast-2.amazonaws.com'

UPLOAD_FOLDER = '/uplouds'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# home page
@app.route('/', methods = ['GET','POST']) 
def index():
    if  request.method == 'POST':
        file = request.files['file']
        file.filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        files = [('file', (file.filename, open(filepath, 'rb'), 'image/jpeg'))]
        response = requests.post(url=URL+'/images', files=files)
        image_name = response.json()['fileName']
        return redirect(f'/image/{image_name}')

    response = requests.get(f'{URL}/images')
    images = response.json()['data']

    return render_template('index.jinja', S3_URL=S3_URL , images=images)
#image page
@app.route("/image/<string:image_name>")
def image(image_name):
    return render_template('image.jinja',image_name=image_name)


@app.route("/image/<string:image_name>/filter")
def image_filter(image_name):
    return render_template('imageFilter.jinja', image_name=image_name)

#اضافتهم
app.register_blueprint(actionbp)
app.register_blueprint(filterbp)

app.run()



