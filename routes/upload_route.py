
from werkzeug.utils import secure_filename
import fitz 
from utils.upload_route.get_bad_pages import get_bad_pages

from classes.File import FILE

ALLOWED_EXTENSIONS = ['pdf']

def upload_route():
    file_name = 'toc.pdf'
    file_path = 'C:\\Users\\Julian\\Desktop\\record_server\\toc.pdf'

    allow_file = allowed_file(file_name)
    if allow_file == True:
        file_name = secure_filename(file_name)
        bad_pages = get_bad_pages(file_path)
        doc = fitz.open(file_path)
        
        FILE.file_name = file_name
        FILE.file_path = file_path
        FILE.bad_pages = bad_pages
        FILE.doc = doc

        return {
            'file_path': file_path,
            'file_name': file_name,
            'bad_pages': bad_pages
        }
    else:
        return {}


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS