from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request
import os.path

app = Flask(__name__)
app.debug = True

# filesystem
app.config['UPLOAD'] = './data'

# cors
cors = CORS(app)


@app.route('/hello', methods=['GET'])
def hello():
    return "hello world"


@app.route('/upload', methods=['POST'])
def upload():
    try:
        for file in request.files.getlist('files'):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD'], filename))
    except Exception as e:
        return bad_request(str(e))
    return "OK"


def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 500
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
