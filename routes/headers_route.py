import json
import re
import fitz

# from classes.File import FILE
from classes.Header import Header

""" 
Starting page number.
Fix any errors.
"""


def headers_route(form, tmpPath):
    pageRange = form['pageRange']
    # position = form['position']
    rangeValue = form['rangeValue']
    titlesList = form['titlesList']
    headerText = form['headerText']
    startNumber = form['startingPageNumber']

    titlesListToJson = json.loads(titlesList)

    # Figure out how to combine the titles and the page numbers.

    if len(titlesListToJson) > 0:
        titles(titlesListToJson, tmpPath)

    # Handle the page numbers first.
    if rangeValue == 'Pages From':
        pageRangeToJson = json.loads(pageRange)
        startingPageNumber = int(pageRangeToJson['start'])
        endingPageNumber = int(pageRangeToJson['end'])
        specific_pages(startingPageNumber, endingPageNumber,
                       headerText, startNumber, tmpPath)
    elif rangeValue == 'All':
        all_pages(headerText, startNumber, tmpPath)

    return {}


def titles(titlesList, tmpPath):
    doc = fitz.open(tmpPath)
    for title in titlesList:
        pageNumber = int(title['pageNumber'])
        page = doc.loadPage(pageNumber - 1)
        header = Header(title['title'])
        page.insertText((header.x, header.y),
                        title['title'], fontsize=12, fontname='Times-Bold')

    doc.saveIncr()


def create_number_with_format(number, form):
    pattern = r'<<\d+>>'
    double_back_arrow = r'<<'
    double_front_arrow = r'>>'
    replacement = '<<%s>>' % number
    new_number = re.sub(pattern, replacement, form)
    new_number = re.sub(double_back_arrow, '', new_number)
    new_number = re.sub(double_front_arrow, '', new_number)
    return new_number


def specific_pages(start, end, headerText, startNumber, tmpPath):
    # doc = FILE.doc
    doc = fitz.open(tmpPath)
    startNumber = int(startNumber)

    for i in range(start, end + 1):
        page = doc.loadPage(i - 1)
        curr_page_number = create_number_with_format(
            str(startNumber), headerText)
        header = Header(curr_page_number)
        page.insertText((header.x, header.y), curr_page_number,
                        fontsize=12, fontname='Times-Bold')
        startNumber = startNumber + 1

    doc.saveIncr()


def all_pages(headerText, startNumber, tmpPath):
    # doc = FILE.doc
    doc = fitz.open(tmpPath)
    startNumber = int(startNumber)

    for i in range(0, doc.pageCount):
        page = doc.loadPage(i)
        curr_page_number = create_number_with_format(
            str(startNumber), headerText)
        header = Header(curr_page_number)
        page.insertText((header.x, header.y), curr_page_number,
                        fontsize=12, fontname='Times-Bold')
        startNumber = startNumber + 1

    doc.saveIncr()