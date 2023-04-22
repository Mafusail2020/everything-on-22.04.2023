class Cell:
    def __init__(self, value):
        self.value = value


class Game:
    EMPTY = "#"
    CELL_X = "X"
    CELL_O = "O"

    def __init__(self):
        self.POLE = [[Cell(self.EMPTY), Cell(self.EMPTY), Cell(self.EMPTY)] for _ in range(3)]
        self.__show_pole()

        self.start_game()

    def is_win(self):
        for row in self.POLE:
            if all(x.value == "X" for x in row):
                if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                    self.__init__()
                    return True
                return False
            if all(o.value == "O" for o in row):
                if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                    self.__init__()
                    return True
                return False

        if all(row[0].value == "O" for row in self.POLE):
            if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if all(row[1].value == "O" for row in self.POLE):
            if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if all(row[2].value == "O" for row in self.POLE):
            if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False

        if all(row[0].value == "X" for row in self.POLE):
            if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if all(row[1].value == "X" for row in self.POLE):
            if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if all(row[2].value == "X" for row in self.POLE):
            if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False

        if self.POLE[0][0].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][2].value == "X":
            if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if self.POLE[0][2].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][0].value == "X":
            if input("Player 1 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False

        if self.POLE[0][0].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][2].value == "O":
            if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__()
                return True
            return False
        if self.POLE[0][2].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][0].value == "O":
            if input("Player 2 won!!! Want to play again? (y/n): ").lower() == 'y':
                self.__init__(); return True
            return False

        return True

    def start_game(self):
        self.player_1()
        self.player_2()

    def __show_pole(self):
        for row in self.POLE:
            for cell in row:
                print(cell.value, end=" ")
            print()
        print("\n---------------------\n")

    def player_1(self):
        row, col = map(int, input("Player 1 to move! Choose an id to set the X: ").split())
        if self.POLE[row][col].value != self.EMPTY:
            print("This cell is occupied!")
            self.player_1()
            return

        self.POLE[row][col].value = self.CELL_X
        self.__show_pole()

    def player_2(self):
        row, col = map(int, input("Player 2 to move! Choose an id to set the O: ").split())
        if self.POLE[row][col].value != self.EMPTY:
            print("This cell is occupied!")
            self.player_1()
            return

        self.POLE[row][col].value = self.CELL_O
        self.__show_pole()

    def __setattr__(self, key, value):
        if key in ('row', 'col') and not 0 <= value <= 2:
            raise ValueError("Id of cell must be in range of 0 and 2!")
        return object.__setattr__(self, key, value)


def game():
    g = Game()
    while g.is_win():
        g.start_game()


if __name__ == "__main__":
    game()
