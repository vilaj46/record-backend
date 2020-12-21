class Header():
    def __init__(self, text):
        self.text = text
        self.x = self.setX(text)
        self.y = self.setY()

    def setX(self, text):
        # Set the x position based on the length of the text
        length_of_text = len(text)

    def setY(self):
        # Set the y position probably based on the position.
        return 30
