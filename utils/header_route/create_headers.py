import json
import fitz

from classes.Header import Header
from utils.header_route.create_titles_list_obj import create_titles_list_obj
from utils.header_route.all_pages import all_pages
from utils.header_route.pages_from import pages_from
from utils.header_route.titles_only import titles_only


"""
Determines what page numbers if any require page numbers.
Otherwise, we just apply titles.
"""


def create_headers(form):
    rangeValue = form['rangeValue']
    titlesList = form['titlesList']

    titlesListToJson = json.loads(titlesList)

    titlesObject = create_titles_list_obj(titlesListToJson)
    headers = {}

    if rangeValue == 'All':
        headers = all_pages(form, titlesObject)
    elif rangeValue == 'Pages From':
        headers = pages_from(form, titlesObject)
    else:
        headers = titles_only(form, titlesObject)

    return headers
