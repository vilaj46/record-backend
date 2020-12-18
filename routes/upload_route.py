
from werkzeug.utils import secure_filename
import fitz
from utils.upload_route.get_bad_pages import get_bad_pages

from classes.File import FILE

ALLOWED_EXTENSIONS = ['pdf']


def upload_route(fileStorage):
    file_name = fileStorage.filename

    allow_file = allowed_file(file_name)

    if allow_file == True:
        fileStream = fileStorage.stream.read()
        doc = fitz.open(stream=fileStream, filetype='pdf')

        file_name = secure_filename(file_name)
        bad_pages = get_bad_pages(doc)

        FILE.file_name = file_name
        FILE.bad_pages = bad_pages
        FILE.doc = doc

        return {
            'file_name': file_name,
            'bad_pages': bad_pages,
            'stream': fileStream
        }
    else:
        return {}


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
