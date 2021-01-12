import random
import fitz

from utils.misc.tmpPath import tmpPath


class TOCEntry:
    def __init__(self, entry, pageNumberInPdf, total_toc_pages):
        self.data = self.default_values()
        self.data['entry'] = entry

        if len(entry) != 0:
            self.data['originalText'] = entry

        if pageNumberInPdf != False:
            self.data['pageNumberInPdf'] = int(pageNumberInPdf)
            self.data['pageNumberForMe'] = int(pageNumberInPdf) - 1

            path = tmpPath()
            doc = fitz.open(path)

            if self.data['pageNumberInPdf'] > doc.pageCount:
                self.data['pageNumberError'] = True

            doc.close()

    def default_values(self):
        idNumber = random.randrange(1000000)

        return {
            'entry': '',  # String
            'originalText': '',  # String
            'idNumber': idNumber,  # String
            'edits': [],  # Array
            'pageNumberInPdf': False,  # String
            'pageNumberForMe': False,  # String
            'textError': False,  # Boolean
            'pageNumberError': False,  # Boolean
        }
