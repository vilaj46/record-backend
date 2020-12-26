def create_titles_list_obj(titles):
    obj = {}

    for title in titles:
        titleLen = len(title['title'])
        pageNumberLen = len(title['pageNumber'])

        if titleLen > 0 and pageNumberLen > 0:
            pageNumber = title['pageNumber']
            obj[pageNumber] = title

    return obj
