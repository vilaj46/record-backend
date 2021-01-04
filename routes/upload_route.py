
import fitz
from werkzeug.utils import secure_filename

from utils.upload_route.get_bad_pages import get_bad_pages
from utils.misc.tmpPath import tmpPath
from utils.misc.allowed_file import allowed_file


def upload_route(fileStorage):
    fileName = fileStorage.filename
    allowFile = allowed_file(fileName)

    path = tmpPath()

    if allowFile == True:
        fileStream = fileStorage.stream.read()

        doc = fitz.open(stream=fileStream, filetype='pdf')

        doc.save(path)

        fileName = secure_filename(fileName)

        return {
            'fileName': fileName,
            'pageCount': doc.pageCount
        }
    else:
        return {}
