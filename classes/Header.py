""" PDF could have 612x792 dimensions.

The horizontal center would be: 306
"""


class Header():
    def __init__(self, headerText, pageNumber, title):
        self.pageNumber = pageNumber
        self.headerText = headerText
        # self.x = self.setX(pageNumber)
        # self.y = self.setY()
        self.lines = self.setLines(pageNumber, title)

    # Set the x position based on the length of the pageNumber
    def setX(self, text):
        length_of_text = len(text)
        return 306 - length_of_text - 1

    # Set the y position probably based on the position.
    def setY(self):
        return 33

    # Figure out how many lines of pageNumber.
    # Figure out each lines position.
    def setLines(self, pageNumber, title):
        lines = []

        if title == None:
            # Set only page number.
            x = self.setX(str(pageNumber))
            line = {'text': str(pageNumber + 1), 'x': x, 'y': 33}
            lines.append(line)
        else:
            # Configure page number and title.
            text = title['title']
            x = self.setX(str(pageNumber))
            line = {'text': str(pageNumber + 1), 'x': x, 'y': 33}
            lines.append(line)
            x = self.setX(text)
            line = {'text': text, 'x': x, 'y': 43}
            lines.append(line)

        return lines
