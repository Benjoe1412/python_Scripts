from tkinter import *  
from subprocess import Popen
import os
from os import walk
import socket
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__,template_folder= 'tempelates')


app.config['UPLOAD_FOLDER'] = "files/"
app.config['MAX_CONTENT_PATH'] = 104857600


@app.route('/upload')
def upload_file():
   return render_template('upload.html', ip = ipAdd + "uploader",ipH = ipAdd)
	

@app.route('/upload', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(app.config['UPLOAD_FOLDER']+filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


	return render_template('upload.html')

@app.route('/')
def index():
    return render_template('index.html',ip = ipAdd+"pictures", ipU= ipAdd + "upload")


@app.route('/pictures')
def video_feed():
    files = []
    files = next(walk(app.config['UPLOAD_FOLDER']), (None, None, []))[2]
    print(files) 
    return render_template('pictures.html', pics = files[0])

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
ipAdd = "http://" + local_ip + ":5000/" 


app.run(host='0.0.0.0', debug=False)