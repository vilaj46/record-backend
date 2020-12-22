""" PDF could have 612x792 dimensions.

The horizontal center would be: 306
"""


class Header():
    def __init__(self, text):
        self.text = text
        self.x = self.setX(text)
        self.y = self.setY()

    # Set the x position based on the length of the text
    def setX(self, text):
        length_of_text = len(text)
        return 306 - length_of_text - 1

    # Set the y position probably based on the position.
    def setY(self):
        return 33
