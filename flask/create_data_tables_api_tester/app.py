from flask import Flask, send_file, request, render_template, redirect, url_for
import requests
from io import BytesIO
import os
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.jinja")

@app.route('/createtable', methods=["POST"])
def createtable():
    filename = request.form["filename"]
    row = int(request.form["row"])
    file_type = request.form["type"]

    data = {"row":row, "type":file_type, "filename":filename}
    header = {'Content-Type': 'application/json'}
    file = requests.post('http://127.0.0.1:8000/createtable', headers = header, json = data)

    if file_type == 'csv':
        mimetype_value = 'application/csv'
    elif file_type == 'db':
        mimetype_value = "application/x-sqlite3"
    elif file_type == 'xlsx':
        mimetype_value = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif file_type == 'html':
        mimetype_value = 'text/html'
    #list
    return send_file(BytesIO(file.content), mimetype=mimetype_value , as_attachment=True, download_name=f"table_{filename}.{file_type}")


@app.route('/createtable/html', methods=["POST"])
def createtable_html():
    filename = request.form["filename"]
    weburl = request.form["weburl"]
    tablenum = request.form["tablenum"]
    file_type = request.form["type"]

    data = {"filename":filename, "type":file_type, "weburl":weburl, "tablenum":tablenum}
    header = {'Content-Type': 'application/json'}
    file = requests.post('http://127.0.0.1:8000/createtable/html', json=data,headers = header)

    if file_type == 'csv':
        mimetype_value = 'application/csv'
    elif file_type == 'db':
        mimetype_value = "application/x-sqlite3"
    elif file_type == 'xlsx':
        mimetype_value = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    #list

    return send_file(BytesIO(file.content), mimetype=mimetype_value, as_attachment=True, download_name=f"table_{filename}.{file_type}")

@app.route('/store', methods=["POST", "GET"])
def store():
    table = request.form["table"]
    return render_template('create_table.jinja', table = table)



app.run(debug=True)


