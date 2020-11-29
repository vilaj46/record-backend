import os
from flask import Flask, request

from routes.upload_route import upload_route
from routes.get_toc_route import get_toc_route
from routes.post_toc_route import post_toc_route 
from routes.delete_toc_entry_route import delete_toc_entry_route
from routes.update_toc_entry_route import update_toc_entry_route

from classes.File import FILE

app = Flask(__name__, instance_relative_config=True)

@app.route('/upload', methods=['POST'])
def upload():
    # Figure out what this does
    upload_data = upload_route()
    upload_data_keys = upload_data.keys()

    if len(upload_data_keys) == 0:
        return {}
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
    else: # PUT
        updated_entry = update_toc_entry_route(id_number, request)
        return updated_entry

app.run(host='0.0.0.0', port=8080, debug=True)