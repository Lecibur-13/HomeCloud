import os

from flask import Flask, request, render_template, jsonify, send_file, send_from_directory, safe_join, abort, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__,template_folder='template')
CORS(app)
app.config['UPLOAD_FOLDER'] = './files'

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/api/uploader', methods=['POST'])
def uploader():

    lista = []
    if request.method == 'POST':
        f = request.files['archivo']
        fileName = secure_filename(f.filename)
        json = {'status' : 'True'}
        lista.append(json)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))

        return jsonify(lista)


@app.route('/api/list', methods=['GET'])
def files():
    index = 0
    lista = []
    files = tuple(os.listdir(app.config['UPLOAD_FOLDER']))
    for file in files:
        index += 1
        split = file.split('.')
        type = split[len(split) - 1]
        jsonFile = {f'name': file, 'type': type}
        lista.append(jsonFile)
    return jsonify(lista)

@app.route('/api/listImg', methods=['GET'])
def files():
    index = 0
    lista = []
    files = tuple(os.listdir(app.config['UPLOAD_FOLDER']))
    for file in files:
        index += 1
        split = file.split('.')
        type = split[len(split) - 1]
        jsonFile = {f'name': file, 'type': type}

        if type == 'jpg' or type == 'jpeg' or type == 'png' or type == 'gif':
            lista.append(jsonFile)
    return jsonify(lista)

@app.route("/api/get/<path:filename>")
def getImg(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run('192.168.1.245')

