import fitz
from classes.File import FILE

from utils.get_toc_route.unify_dots import unify_dots
from utils.get_toc_route.remove_new_lines import remove_new_lines
from utils.get_toc_route.get_entries_from_page import get_entries_from_page
from utils.get_toc_route.set_certification_page_number import set_certification_page_number
# \xc2\xa7 = §

# If our entries / page_numbers are not equal,
# gather the entire text then try and find the entries.

def get_toc_route():
    # doc = FILE.doc
    file_path = 'C:\\Users\\Julian\\Desktop\\record_server\\toc.pdf'
    doc = fitz.open(file_path)

    entries = []

    for i in range(doc.pageCount):
        page = doc.loadPage(i)
        text = page.getText()
        text = text.encode("utf-8")
        
        text = str(text)
        text_without_dots = unify_dots(text)
        text_without_new_lines = remove_new_lines(text_without_dots)

        entries_per_page = get_entries_from_page(text_without_new_lines, i, doc.pageCount)
        entries += entries_per_page
    FILE.entries = entries
    FILE.difference_in_page_numbers = entries[0]['page_num_for_me'] - entries[0]['page_num_in_pdf']

    set_certification_page_number()

    return {
        'entries': entries
    }
