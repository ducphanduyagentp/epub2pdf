from flask import *
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import subprocess
import hashlib

UPLOAD_FOLDER = "./samples/"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

users = {
    "yeet": generate_password_hash("yeet"),
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')


@app.route('/nothing', methods=["POST"])
@auth.login_required
def nothing():
    f = request.files['input_file']
    file_content = f.read()
    file_hash = hashlib.md5(file_content).hexdigest()
    save_file = UPLOAD_FOLDER + 'input-%s.epub' % file_hash
    fp = open(save_file, 'wb')
    fp.write(file_content)
    fp.close()
    f.close()
    try:
        subprocess.check_output(['ebook-convert', UPLOAD_FOLDER + 'input-%s.epub' % file_hash, UPLOAD_FOLDER + 'output-%s.pdf' % file_hash])
        return send_file(UPLOAD_FOLDER + 'output-%s.pdf' % file_hash, as_attachment=True)
    except:
        return "failed."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)

