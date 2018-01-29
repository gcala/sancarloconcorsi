import os
from flask import Flask, render_template, send_file, request, redirect, url_for, send_from_directory
#from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from werkzeug import secure_filename
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
