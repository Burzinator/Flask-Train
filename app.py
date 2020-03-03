from flask import Flask, url_for, request, redirect, make_response, render_template, session, escape
from werkzeug.utils import secure_filename
import os

folder = "C:/Users/Andy/Documents/Projekte"
extensions = {'txt', 'jpg', 'png', 'pdf'}
app = Flask(__name__)
app.secret_key='ab\xe8{F>bnCSs\xb6\xf0Y\xb5B\xef\xcfw{\xea\xf2\x90p+2'


#index
@app.route("/")
def index():
    return render_template('index.html')

#Prüfen ob hochgeladene Datei erlaubt ist
def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

#upload
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url) and '''<h1>Uploadfehler</h1>'''
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url) and '''<h1>kein File ausgewählt</h1>'''
        if allowed(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return redirect(request.url) and '''<h1>Upload erfolgreich</h1>'''

    return render_template('upload.html')

#login
@app.route("/login")
def login():
    return render_template('login.html', spaß="Hier loggst du dich ein")



#login erfolgreich
@app.route("/login_done", methods=['POST', 'GET'])
def sessions():

    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
            return "Hallo " + escape(session['name']) + "!"
        else:
            return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('name', None)
    return render_template('login.html')


if __name__=="__main__":
    app.run(debug=True)
