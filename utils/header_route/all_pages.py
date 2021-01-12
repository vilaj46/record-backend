import fitz

from utils.misc.tmpPath import tmpPath
from classes.Header import Header


"""
Set the headers / titles.
"""


def all_pages(form, titlesObject):
    path = tmpPath()
    currentPageNumber = int(form['startingPageNumber'])
    doc = fitz.open(path)

    headers = []

    for i in range(0, doc.pageCount):
        header = None
        pages = {'pageNumberText': currentPageNumber, 'pageNumberInDoc': i}

        try:
            # There is a title on this page.
            # The error will catch in the title assignment
            # if there is no key associated with the page number.
            # currentPageNumberString = str(currentPageNumber)
            title = titlesObject[str(currentPageNumber)]
            header = Header(form, pages, title, True)
        except:
            # There is not a title on this page.
            header = Header(form, pages, None, True)

        headers.append(header)

        currentPageNumber = currentPageNumber + 1

    doc.close()

    return headers
