import os
from flask import Flask, request, send_file
from flask_cors import CORS
import fitz
import tempfile


from routes.headers import headers_route
from routes.upload_route import upload_route
from routes.get_toc_route import get_toc_route
from routes.post_toc_route import post_toc_route
from routes.delete_toc_entry_route import delete_toc_entry_route
from routes.update_toc_entry_route import update_toc_entry_route

from classes.File import FILE

app = Flask(__name__, instance_relative_config=True)
CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

tmp_path = '/tmp/test.pdf'
# tmp_path = './tmp/test.pdf'


@app.route('/')
def index():
    return 'Index Page'


@app.route('/upload', methods=['POST'])
def upload():
    upload_data = upload_route(request.files['file'], tmp_path)
    upload_data_keys = upload_data.keys()

    # file1 = request.files['file']
    # fileStream = file1.stream.read()
    # doc = fitz.open(stream=fileStream, filetype='pdf')

    # doc.save('/tmp/test.pdf')
    # return send_file('/tmp/test.pdf')
    if len(upload_data_keys) == 0:
        return 'Bad request!', 400
    else:
        return upload_data


@app.route('/toc', methods=['GET', 'POST'])
def toc():
    if request.method == 'GET':
        toc_data = get_toc_route()
        return toc_data
    else:
        new_entry = post_toc_route(request)
        return new_entry


# We are on the PUT method.
# Change page number functionality
# Error checks fuctionality as well.

# Figure out what we want to return for both
# PUT and delete. Do we want to have a general entry errors for all of them
# or a page number errors for all of them. Incorporate the certification page
# number when calculating the page_number_in_pdf error.

@app.route('/toc/<id_number>', methods=['DELETE', 'PUT'])
def toc_id_number(id_number):
    # entries = FILE.entries

    if request.method == 'DELETE':
        deleted_entry = delete_toc_entry_route(id_number, request)
        return deleted_entry
    else:  # PUT
        updated_entry = update_toc_entry_route(id_number, request)
        return updated_entry


@app.route('/headers', methods=['POST'])
def headers():
    headers_route(request.form, tmp_path)

    # doc = FILE.doc

    # return {}
    # doc.save('/tmp/test.pdf')
    # return send_file('/tmp/test.pdf')
    # doc.save('./tmp/test.pdf')
    return send_file(tmp_path)


# app.run(host='localhost', port=8080, debug=True)
if __name__ == '__main__':
    app.run()
