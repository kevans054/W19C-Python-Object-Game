class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    
    # TODO
    # def moveUp(self):
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1
        
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1
        
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1

    def moveRight(self):
        self.columnPosition = self.columnPosition + 1
        