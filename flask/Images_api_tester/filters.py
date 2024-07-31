from flask import Blueprint, request, send_file, jsonify, current_app, render_template
import requests, datetime
#يخزن معلومات موقتا بالذاكرة
from io import BytesIO

bp = Blueprint('filter', __name__)


# blur
@bp.route('/blur', methods=["POST"])
def blur():
    if request.method == 'POST':
            radius = int(request.form['radius'])
            data = {'filename': request.form['filename'], "radius":radius}

            response = requests.post(url=current_app.config['URL']+'/filters/blur', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'filter_{request.form["filename"]}')

# contrast
@bp.route('/contrast', methods=["POST"])
def contrast():
    if request.method == 'POST':
            factor = float(request.form['factor'])
            data = {'filename': request.form['filename'], "factor":factor}

            response = requests.post(url=current_app.config['URL']+'/filters/contrast', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'filter_{request.form["filename"]}')


# brightness
@bp.route('/brightness', methods=["POST"])
def brightness():
    if request.method == 'POST':
            factor = request.form['factor']
            data = {'filename': request.form['filename'], "factor":factor}

            response = requests.post(url=current_app.config['URL']+'/filters/brightness', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'filter_{request.form["filename"]}')



# android
@bp.route('/android', methods=["POST"])
def android():
     if request.method == 'POST':
            data = {'filename': request.form['filename']}
            response = requests.post(url=current_app.config['URL']+'/android', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='application/zip', as_attachment=True, download_name=f'{str(datetime.datetime.timestamp(datetime.datetime.now())).rsplit('.')[0]}.zip')




