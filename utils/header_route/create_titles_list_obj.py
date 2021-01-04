"""
Puts our list of titles in a dictionary 
with the page number as the key. This will
make it so that it is easier to access once we are 
creating the headers.
"""


def create_titles_list_obj(titles):
    obj = {}

    for title in titles:
        titleLen = len(title['entry'])
        pageNumberLen = len(str(title['pageNumberInPdf']))

        # Will only add the title if we have a text and page number.
        if titleLen > 0 and pageNumberLen > 0:
            pageNumber = title['pageNumberInPdf']
            obj[pageNumber] = title

    return obj
