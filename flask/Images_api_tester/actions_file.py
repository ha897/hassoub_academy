from flask import Blueprint, request, send_file, jsonify, current_app, render_template
import requests
from io import BytesIO

bp = Blueprint('actions_file', __name__)



#resize
@bp.route('/resize', methods=['POST'])
def resize():
    if request.method == 'POST':
        data = {'filename': request.form['filename'], 'width': request.form['width'], 'height': request.form['height']}
        response = requests.post(url=current_app.config['URL'] +'/actions/resize', json=data, headers = {'Content-Type': 'application/json'})
        return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'resized_{request.form["filename"]}')

#presets resize
@bp.route('/presets', methods=["POST"])
def resize_presets():
    preset = request.form['preset']
    if request.method == 'POST':
            presets = {'small': (640, 480), 'medium': (1280, 960), 'large': (1600, 1200)}

            if preset not in presets:
                    return jsonify({'message': 'The preset is not available'}), 400
            
            data = {'filename': request.form['filename']}


            response = requests.post(url=current_app.config['URL'] +'/actions/presets/'+preset, json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'resized_{request.form["filename"]}')


# rotate
@bp.route('/rotate', methods=["POST"])
def rotate():
    degree = int(request.form['degree'])
    if request.method == 'POST':
            data = {'filename': request.form['filename'], "degree":degree}

            response = requests.post(url=current_app.config['URL'] +'/actions/rotate', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'resized_{request.form["filename"]}')
    
# flip
@bp.route('/flip', methods=["POST"])
def flip():
    direction = request.form['direction']
    if request.method == 'POST':
            data = {'filename': request.form['filename'], "direction":direction}

            response = requests.post(url=current_app.config['URL'] +'/actions/flip', json=data, headers = {'Content-Type': 'application/json'})
            return send_file(BytesIO(response.content), mimetype='image/jpeg', as_attachment=True, download_name=f'resized_{request.form["filename"]}')
