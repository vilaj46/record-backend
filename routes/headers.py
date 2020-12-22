import json
import re

from classes.File import FILE
from classes.Header import Header

""" 
Starting page number.
Fix any errors.
"""


def headers_route(form):
    pageRange = form['pageRange']
    # position = form['position']
    rangeValue = form['rangeValue']
    # titlesList = form['titlesList']
    headerText = form['headerText']
    startNumber = form['startingPageNumber']

    # Handle the page numbers first.
    if rangeValue == 'Pages From':
        pageRangeToJson = json.loads(pageRange)
        startingPageNumber = int(pageRangeToJson['start'])
        endingPageNumber = int(pageRangeToJson['end'])
        specific_pages(startingPageNumber, endingPageNumber)
    elif rangeValue == 'All':
        all_pages(headerText, startNumber)

    return {}


def create_number_with_format(number, form):
    pattern = r'<<\d+>>'
    double_back_arrow = r'<<'
    double_front_arrow = r'>>'
    replacement = '<<%s>>' % number
    new_number = re.sub(pattern, replacement, form)
    new_number = re.sub(double_back_arrow, '', new_number)
    new_number = re.sub(double_front_arrow, '', new_number)
    return new_number


def specific_pages(start, end):
    doc = FILE.doc
    for i in range(start, end + 1):
        page = doc.loadPage(i)
        curr_page_number = str(i + 1)
        header = Header(curr_page_number)
        page.insertText((header.x, header.y), curr_page_number,
                        fontsize=12, fontname='Times-Bold')


def all_pages(headerText, startNumber):
    doc = FILE.doc
    print(doc)
    startNumber = int(startNumber)

    for i in range(0, doc.pageCount):
        page = doc.loadPage(i)
        curr_page_number = create_number_with_format(
            str(startNumber), headerText)
        header = Header(curr_page_number)
        page.insertText((header.x, header.y), curr_page_number,
                        fontsize=12, fontname='Times-Bold')
        startNumber = startNumber + 1
