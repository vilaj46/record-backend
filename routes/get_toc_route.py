import fitz
from werkzeug.utils import secure_filename

from utils.get_toc_route.unify_dots import unify_dots
from utils.get_toc_route.remove_new_lines import remove_new_lines
from utils.get_toc_route.get_entries_from_page import get_entries_from_page
from utils.misc.tmpToc import tmpToc
from utils.misc.allowed_file import allowed_file

# \xc2\xa7 = §

# If our entries / page_numbers are not equal,
# gather the entire text then try and find the entries.


def get_toc_route(fileStorage):
    fileName = fileStorage.filename
    allowFile = allowed_file(fileName)

    if allowFile == True:
        tmpPath = tmpToc()
        fileStream = fileStorage.stream.read()

        doc = fitz.open(stream=fileStream, filetype='pdf')

        doc.save(tmpPath)

        fileName = secure_filename(fileName)

        entries = []

        for i in range(doc.pageCount):
            page = doc.loadPage(i)
            text = page.getText()
            text = text.encode("utf-8")

            text = str(text)
            textWithoutDots = unify_dots(text)
            textWithoutLines = remove_new_lines(textWithoutDots)

            entriesPerPage = get_entries_from_page(
                textWithoutLines, i, doc.pageCount)
            entries += entriesPerPage
            # difference = entries[0]['pageNumberForMe'] - \
            #     entries[0]['pageNumberInPdf']

        return {
            'entries': entries
        }
    else:
        return {}
