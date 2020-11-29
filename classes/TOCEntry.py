import random

class TOCEntry:
    def __init__(self, entry, page_num_in_pdf, total_toc_pages):
        self.data = self.default_values()
        self.data['entry'] = entry

        if len(entry) != 0:
            self.data['original_text'] = entry

        if page_num_in_pdf != False:
            self.data['page_num_in_pdf'] = page_num_in_pdf
            self.data['page_num_for_me'] = page_num_in_pdf + total_toc_pages


    def default_values(self):
        id_number = random.randrange(1000000)
        return {
            'entry': '', # String
            'original_text': '', # String
            'id_number': id_number, # String
            'edits': [], # Array
            'page_num_in_pdf': False, # String
            'page_num_for_me': False, # String
            'text_error': False, # Boolean
            'page_number_error': False, # Boolean
        }