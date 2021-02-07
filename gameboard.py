class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 6
        self.board = [
            [" * ", " * ",  " * ", " * ", " * ", "   ", " * ", " * ", " * ", " * "],
            [#row1
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [#row2
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                "   ",
                " * ",
            ],
            [#row3
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
             [#row4
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
                " * ",
                " * ",
                " * ",
            ],
             [#row5
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
             [#row6
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [#row7
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [#row8
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [#row9
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [#row10
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print("P ", end=" ")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there! Try again.")
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if playerRow == 0 and playerColumn == 5:
            return True
        return False
