import re

""" PDF could have 612x792 dimensions.

The horizontal center would be: 303
Y values are 11 apart.
"""


class Header():

    """
    Grab the necessary values first.

    Then set the header values we will need to set the header.
    """

    def __init__(self, form, pages, title, includePageNumber):
        headerText = form['headerText']
        pageNumberText = pages['pageNumberText']
        pageNumberInDoc = pages['pageNumberInDoc']

        self.form = form
        self.includePageNumber = includePageNumber
        self.pageNumberText = pageNumberText
        self.pageNumberInDoc = pageNumberInDoc
        self.headerText = headerText
        self.lines = self.setLines(title)

    """
    Set the y position based on the position.

    ** THIS IS NOT IMPLEMENETED YET **
    """

    def setY(self):
        return 33

    """
    Grabs the page number then formats it.
    If there is a title, we set the title as the second line.
    """

    def setLines(self, title):
        lines = []
        pageNumberText = self.pageNumberText
        pageNumberFormatted = self.create_number_with_format(
            str(pageNumberText), self.headerText)

        if self.includePageNumber:
            line = {'text': pageNumberFormatted, 'y': 22}
            lines.append(line)

        # Set title if it exists.
        if title != None:
            text = title['entry']
            line = {}

            print(title)

            if self.includePageNumber:
                line = {'text': text, 'y': 33}
            else:
                line = {'text': text, 'y': 22}
            lines.append(line)

        return lines

    """
    Keeps the prepend and append text but replaces
    the number between the arrows.
    """

    def create_number_with_format(self, number, format1):
        pattern = r'<<\d+>>'
        double_back_arrow = r'<<'
        double_front_arrow = r'>>'
        replacement = '<<%s>>' % number
        new_number = re.sub(pattern, replacement, format1)
        new_number = re.sub(double_back_arrow, '', new_number)
        new_number = re.sub(double_front_arrow, '', new_number)
        return new_number
