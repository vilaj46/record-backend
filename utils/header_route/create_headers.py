import json
import fitz

from classes.Header import Header
from utils.header_route.create_titles_list_obj import create_titles_list_obj


def create_headers(form, tmpPath):
    # pageRange = form['pageRange']
    # position = form['position']
    # rangeValue = form['rangeValue']
    titlesList = form['titlesList']
    # headerText = form['headerText']
    # startNumber = form['startingPageNumber']

    titlesListToJson = json.loads(titlesList)

    # Create a list of headers with the given information.
    # Create a titles list object based on the page numbers so we only have to iterate over once.
    titlesObject = create_titles_list_obj(titlesListToJson)

    headers = all_pages(form, titlesObject, tmpPath)

    return headers


def all_pages(form, titlesObject, tmpPath):
    pageNumber = form['startingPageNumber']
    startNumber = int(form['startingPageNumber'])
    headerText = form['headerText']
    doc = fitz.open(tmpPath)

    headers = []

    for i in range(0, doc.pageCount):
        header = None

        try:
            # There is a title on this page.
            title = titlesObject[pageNumber]
            header = Header(headerText, i, title)
        except:
            # There is not a title on this page.
            header = Header(headerText, i, None)

        headers.append(header)
        startNumber = startNumber + 1
        pageNumber = int(pageNumber) + 1
        pageNumber = str(pageNumber)

    doc.close()

    return headers
