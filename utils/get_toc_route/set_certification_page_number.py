# from classes.File import FILE

def set_certification_page_number():
    # self.certification_page_number
    entries = FILE.entries
    certification_entry = entries[len(entries) - 1]

    FILE.certification_page_number = certification_entry['page_num_in_pdf']
