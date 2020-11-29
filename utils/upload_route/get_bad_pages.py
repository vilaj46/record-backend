import fitz

def get_bad_pages(file_path):
    doc = fitz.open(file_path)
    page_count = doc.pageCount

    bad_pages = []

    for i in range(page_count):
        page = doc.loadPage(i)
        text = page.getText()
        if len(text) <= 0:
            bad_pages.append(i)

    return bad_pages