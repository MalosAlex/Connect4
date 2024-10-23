from texttable import Texttable, get_color_string, bcolors


class Board:
    def __init__(self):
        self.grid = [[0 for i in range(7)] for j in range(6)]
        self.moves = 0

    def __str__(self):
        table = Texttable()
        table.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m"])
        for row in self.grid:
            str_row = []
            for elem in row:
                if elem == 0:
                    str_row.append("\u200B")
                elif elem == 1:
                    str_row.append(get_color_string(bcolors.RED, "o"))
                elif elem == -1:
                    str_row.append(get_color_string(bcolors.BLUE, "o"))
            table.add_row(str_row)

        result = table.draw()

        return result

    def submit_move(self, column, row, player):
        """
        Makes a move for a player on the board.
        :param column:
        :param row:
        :param player:
        :return: None
        """
        self.grid[row][column] = player

    def get_row(self, column):
        """
        Returns the row of the last move.
        :param column:
        :return:
        """
        for i in range(5, -1, -1):
            if self.grid[i][column] == 0:
                return i
        return -1

    def clone(self):
        """
        Clones the board.
        :return:
        """
        clone = Board()
        clone.grid = [row[:] for row in self.grid]
        return clone

    def get_row_nonempty(self, column):
        """
        Returns the row of the last move.
        :param column:
        :return:
        """
        for i in range(0, 6, 1):
            if self.grid[i][column] != 0:
                return i
        return -1

    def canPlay(self, column):
        """
        Checks if a move can be played in the specified column.
        :param column: The column to check.
        :return: True if a move can be played, False otherwise.
        """
        return self.grid[0][column] == 0

    def play(self, column):
        """
        Plays a move in the specified column.
        :param column: The column to play in.
        :return: None
        """
        row = self.get_row_nonempty(column)
        self.grid[row][column] = 1 if self.moves % 2 == 0 else -1
        self.moves += 1



