import re

""" PDF could have 612x792 dimensions.

The horizontal center would be: 306
"""


class Header():
    def __init__(self, headerText, pageNumberText, pageNumberInDoc, title):
        self.pageNumberText = pageNumberText
        self.pageNumberInDoc = pageNumberInDoc
        self.headerText = headerText
        self.lines = self.setLines(pageNumberText, title)

    # Set the x position based on the length of the pageNumber
    def setX(self, text):
        length_of_text = len(text)
        return 306 - length_of_text - 1

    # Set the y position probably based on the position.
    def setY(self):
        return 33

    # Figure out how many lines of pageNumber.
    # Figure out each lines position.
    def setLines(self, pageNumberText, title):
        lines = []

        if title == None:
            # Set only page number.
            x = self.setX(str(pageNumberText))

            pageNumberFormatted = self.create_number_with_format(
                str(pageNumberText), self.headerText)
            line = {'text': pageNumberFormatted, 'x': x, 'y': 33}
            lines.append(line)
        else:
            # Configure page number and title.
            text = title['title']
            x = self.setX(str(pageNumberText))
            pageNumberFormatted = self.create_number_with_format(
                str(pageNumberText), self.headerText)
            line = {'text': pageNumberFormatted, 'x': x, 'y': 33}
            lines.append(line)
            x = self.setX(text)
            line = {'text': text, 'x': x, 'y': 43}
            lines.append(line)

        return lines

    def create_number_with_format(self, number, form):
        pattern = r'<<\d+>>'
        double_back_arrow = r'<<'
        double_front_arrow = r'>>'
        replacement = '<<%s>>' % number
        new_number = re.sub(pattern, replacement, form)
        new_number = re.sub(double_back_arrow, '', new_number)
        new_number = re.sub(double_front_arrow, '', new_number)
        return new_number
