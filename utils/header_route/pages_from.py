import json

from classes.Header import Header

"""
Get the range from the pageRange key.
Set the headers / titles.
"""


def pages_from(form, titlesObject):
    currentPageNumber = int(form['startingPageNumber'])

    pageRange = json.loads(form['pageRange'])
    start = int(pageRange['start'])
    end = int(pageRange['end'])

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
            header = Header(form, pages, title, True)
        except:
            # There is not a title on this page.
            header = Header(form, pages, None, True)

        headers.append(header)

        currentPageNumber = currentPageNumber + 1

    return headers
