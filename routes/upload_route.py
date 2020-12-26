
from werkzeug.utils import secure_filename
import fitz
from utils.upload_route.get_bad_pages import get_bad_pages

ALLOWED_EXTENSIONS = ['pdf']


def upload_route(fileStorage, tmpPath):
    file_name = fileStorage.filename
    allow_file = allowed_file(file_name)

    if allow_file == True:
        fileStream = fileStorage.stream.read()

        doc = fitz.open(stream=fileStream, filetype='pdf')

        doc.save(tmpPath)

        file_name = secure_filename(file_name)

        return {
            'fileName': file_name,
            'pageCount': doc.pageCount
        }
    else:
        return {}


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
