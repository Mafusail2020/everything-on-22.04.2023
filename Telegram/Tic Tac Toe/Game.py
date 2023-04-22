from random import randint


class Cell:
    def __init__(self, val):
        self.value = val


class TicTacToeSolo:
    CELL_EMPTY = "#"
    CELL_X = "X"
    CELL_O = "O"

    def __init__(self):
        self.POLE = [[Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY)] for _ in range(3)]

    def is_win(self):
        for row in self.POLE:
            if all(x.value == "X" for x in row):
                return True
            if all(o.value == "O" for o in row):
                return True

        if all(row[0].value == "O" for row in self.POLE):
            return True
        if all(row[1].value == "O" for row in self.POLE):
            return True
        if all(row[2].value == "O" for row in self.POLE):
            return True

        if all(row[0].value == "X" for row in self.POLE):
            return True
        if all(row[1].value == "X" for row in self.POLE):
            return True
        if all(row[2].value == "X" for row in self.POLE):
            return True

        if self.POLE[0][0].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][2].value == "X":
            return True
        if self.POLE[0][2].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][0].value == "X":
            return True

        if self.POLE[0][0].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][2].value == "O":
            return True
        if self.POLE[0][2].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][0].value == "O":
            return True

        return None

    def return_pole(self):
        pole = ""
        for row in self.POLE:
            for cell in row:
                pole += f"{cell.value} "
            pole += "\n"
        return pole

    def bot_move(self):
        while True:
            row, col = randint(0, 2), randint(0, 2)

            if self.POLE[row][col].value == self.CELL_EMPTY:
                self.POLE[row][col].value = self.CELL_O
                break

    def is_x_valid(self, row: int, col: int):
        if self.POLE[row][col].value == self.CELL_EMPTY:
            return True
        return False

    def set_x(self, row: int, col: int):
        self.POLE[row][col].value = self.CELL_X
        who_won = self.is_win()
        if who_won is not None:
            return who_won
        self.bot_move()
        who_won = self.is_win()
        if who_won is not None:
            return who_won
        return ""


class TicTacToeMult:
    CELL_EMPTY = "#"
    CELL_X = "X"
    CELL_O = "O"

    def __init__(self):
        self.POLE = [[Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY)] for _ in range(3)]

    def is_win(self):
        for row in self.POLE:
            if all(x.value == "X" for x in row):
                return True
            if all(o.value == "O" for o in row):
                return True

        if all(row[0].value == "O" for row in self.POLE):
            return True
        if all(row[1].value == "O" for row in self.POLE):
            return True
        if all(row[2].value == "O" for row in self.POLE):
            return True

        if all(row[0].value == "X" for row in self.POLE):
            return True
        if all(row[1].value == "X" for row in self.POLE):
            return True
        if all(row[2].value == "X" for row in self.POLE):
            return True

        if self.POLE[0][0].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][2].value == "X":
            return True
        if self.POLE[0][2].value == "X" and self.POLE[1][1].value == "X" and self.POLE[2][0].value == "X":
            return True

        if self.POLE[0][0].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][2].value == "O":
            return True
        if self.POLE[0][2].value == "O" and self.POLE[1][1].value == "O" and self.POLE[2][0].value == "O":
            return True

        return None

    def is_cell_valid(self, row: int, col: int):
        if self.POLE[row][col].value == self.CELL_EMPTY:
            return True
        return False

    def return_pole(self):
        pole = ""
        for row in self.POLE:
            for cell in row:
                pole += f"{cell.value} "
            pole += "\n"
        return pole

    def set_x(self, row: int, col: int):
        self.POLE[row][col].value = self.CELL_X
        who_won = self.is_win()
        if who_won is not None:
            return who_won

    def set_o(self, row: int, col: int):
        self.POLE[row][col].value = self.CELL_O
        who_won = self.is_win()
        if who_won is not None:
            return who_won

    def is_tie(self):
        free_row = 3
        for row in self.POLE:
            if all(cell.value != self.CELL_EMPTY for cell in row):
                free_row -= 1

        return True if free_row == 0 else False

    def clear(self):
        self.POLE = [[Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY), Cell(self.CELL_EMPTY)] for _ in range(3)]
