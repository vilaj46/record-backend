from classes.Header import Header


def titles_only(form, titlesObject):
    headers = []

    keys = titlesObject.keys()
    for key in keys:
        # intKey = int(key)
        header = None

        title = titlesObject[key]
        currentPageNumber = int(title['pageNumberInPdf'])
        pages = {'pageNumberText': currentPageNumber,
                 'pageNumberInDoc': currentPageNumber - 1}

        header = Header(form, pages, title, False)

        headers.append(header)

    return headers
