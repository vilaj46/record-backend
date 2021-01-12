import re
import fitz

from classes.Header import Header
from utils.header_route.create_headers import create_headers
from utils.misc.tmpPath import tmpPath

"""
Creates headers with our given information.
Then applies headers to the document.
"""


def headers_route(form):
    path = tmpPath()

    headers = create_headers(form)

    doc = fitz.open(path)

    for header in headers:
        pageNumberInDoc = header.pageNumberInDoc

        try:
            page = doc.loadPage(pageNumberInDoc)

            for line in header.lines:
                rect = fitz.Rect(0, line['y'], 612, 100)
                page.insertTextbox(
                    rect, line['text'], fontsize=12, fontname='Times-Bold', border_width=2, align=1)
        except:
            continue

    doc.saveIncr()
    doc.close()

    return {}
