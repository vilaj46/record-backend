import os
from flask import Flask, request, send_file
from flask_cors import CORS

from routes.headers_route import headers_route
from routes.upload_route import upload_route
from routes.get_toc_route import get_toc_route
from routes.post_toc_route import post_toc_route
from routes.delete_toc_entry_route import delete_toc_entry_route
from routes.update_toc_entry_route import update_toc_entry_route

from utils.misc.tmpPath import tmpPath

app = Flask(__name__, instance_relative_config=True)
CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Import Table of Contents.
# Set page ranges for the titles and the ability to format it.
# Error handling / prevention.
# Check if headers on the page already.
# Fix page number right click on the front end.
# Add 'y' positioning to the headers. Ability to move them at the top or bottom of page.


@app.route('/')
def index():
    return 'Index Page'


@app.route('/upload', methods=['POST'])
def upload():
    upload_data = upload_route(request.files['file'])
    upload_data_keys = upload_data.keys()
    if len(upload_data_keys) == 0:
        return 'Bad request!', 400
    else:
        return upload_data


# @app.route('/toc', methods=['GET', 'POST'])
# def toc():
#     if request.method == 'GET':
#         toc_data = get_toc_route()
#         return toc_data
#     else:
#         new_entry = post_toc_route(request)
#         return new_entry


@app.route('/toc/<id_number>', methods=['DELETE', 'PUT'])
def toc_id_number(id_number):
    if request.method == 'DELETE':
        deleted_entry = delete_toc_entry_route(id_number, request)
        return deleted_entry
    else:  # PUT
        updated_entry = update_toc_entry_route(id_number, request)
        return updated_entry


@app.route('/headers', methods=['POST'])
def headers():
    path = tmpPath()
    headers_route(request.form)
    return send_file(path)


@app.route('/toc', methods=['POST'])
def toc():
    #
    return {}


app.run(host='localhost', port=8080, debug=True)
# if __name__ == '__main__':
#     app.run()
