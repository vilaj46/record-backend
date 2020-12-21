import json
from classes.File import FILE
from classes.Header import Header


def headers_route(form):
    pageRange = form['pageRange']
    position = form['position']
    rangeValue = form['rangeValue']
    titlesList = form['titlesList']

    # Handle the page numbers first.
    if rangeValue != '' and rangeValue != 'None':
        pageRangeToJson = json.loads(pageRange)
        startingPageNumber = pageRangeToJson['start']
        endingPageNumber = pageRangeToJson['end']

    # Set numbers on all pages.
    all_pages()
    # Set numbers on specific page range.

    return {}


def all_pages():
    doc = FILE.doc
    for i in range(0, doc.pageCount):
        page = doc.loadPage(i)
        curr_page_number = str(i + 1)
        header = Header(curr_page_number)
        page.insertText((100, header.y), curr_page_number)

    # doc.save()
