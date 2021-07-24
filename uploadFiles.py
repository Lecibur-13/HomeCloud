import os

from flask import Flask, request, render_template, jsonify, send_file, send_from_directory, safe_join, abort, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = './files'

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/api/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['archivo']
        fileName = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))

        # return url_for('getImg', filename=fileName)


@app.route('/api/list')
def files():
    index = 0
    lista = []
    files = tuple(os.listdir(app.config['UPLOAD_FOLDER']))
    for file in files:
        index += 1
        json = {f'{index}': file}
        lista.append(json)
    return jsonify(lista)

@app.route("/api/get/<path:filename>")
def getImg(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run('10.1.2.6')

