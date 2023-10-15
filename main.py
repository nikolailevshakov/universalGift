from flask import Flask, request, flash, redirect, url_for, send_from_directory, render_template
import utils

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        utils.clear_folder()
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(f'images/{file.filename}')

        who = request.form.get("who")
        name = request.form.get("name")
        template = request.form.get("template")
        utils.generate_certificate(template, file.filename, who, name)

        return redirect('/certificates/cert.jpg')

    return render_template("index.html")


@app.route('/certificates/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
