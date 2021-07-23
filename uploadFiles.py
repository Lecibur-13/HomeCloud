import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = '/Users/csdocsdesarrollo/Documents/homeCloud'

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['archivo']
        fileName = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))

        return 'archivo subido exitosamente'

if __name__ == '__main__':
    app.run(debug=True)

