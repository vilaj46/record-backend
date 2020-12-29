import fitz
import json

from utils.misc.tmpPath import tmpPath
from classes.Header import Header

"""
Get the range from the pageRange key.
Set the headers / titles.
"""


def pages_from(form, titlesObject):
    path = tmpPath()
    currentPageNumber = int(form['startingPageNumber'])

    pageRange = json.loads(form['pageRange'])
    start = int(pageRange['start'])
    end = int(pageRange['end'])

    doc = fitz.open(path)

    headers = []

    for i in range(start - 1, end):
        header = None
        pages = {'pageNumberText': currentPageNumber, 'pageNumberInDoc': i}
        try:
            # There is a title on this page.
            # The error will catch in the title assignment
            # if there is no key associated with the page number.
            currentPageNumberString = str(currentPageNumber)
            title = titlesObject[currentPageNumberString]
            header = Header(form, pages, title)
        except:
            # There is not a title on this page.
            header = Header(form, pages, None)

        headers.append(header)

        currentPageNumber = currentPageNumber + 1

    doc.close()

    return headers
