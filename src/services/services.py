from src.domain.board import Board


class Services:
    def __init__(self, board):
        self.board = board

    def make_move(self, column, player):
        """
        Makes a move for a player on the board.
        :param column: int
        :param player: str
        :return: None
        """
        for i in range(5, -1, -1):
            if self.board.grid[i][column] == 0:
                self.board.submit_move(column, i, player)
                return i

    def check_win(self, player, last_move_column, last_move_row):
        """
        We check around the last move if the player has won.
        :param player:
        :param last_move_column:
        :param last_move_row:
        :return:
        """
        # horizontal check
        ur = 0
        ul = 0
        count_r = 0
        count_l = 0
        for i in range(1, 4):
            if last_move_column + i < 7:
                if self.board.grid[last_move_row][last_move_column+i] == player and ur != -1:
                    count_r += 1
                else:
                    ur = -1
            if last_move_column - i >= 0:
                if self.board.grid[last_move_row][last_move_column - i] == player and ul != -1:
                    count_l += 1
                else:
                    ul = -1
            if count_l + count_r >= 3:
                return True
            if count_l == 3 or count_r == 3:
                return True
            if count_l < i and count_r < i:
                break

        # vertical check
        uc = 0
        ud = 0
        count_u = 0
        count_d = 0
        for i in range(1, 4):
            if last_move_row + i < 6:
                if self.board.grid[last_move_row+i][last_move_column] == player and uc != -1:
                    count_u += 1
                else:
                    uc = -1
            if last_move_row - i >= 0:
                if self.board.grid[last_move_row - i][last_move_column] == player and ud != -1:
                    count_d += 1
                else:
                    ud = -1
            if count_u + count_d == 3:
                return True
            if count_u == 3 or count_d == 3:
                return True
            if count_u < i and count_d < i:
                break

        # diagonal check
        urc = 0
        ulc = 0
        drc = 0
        dlc = 0
        count_ur = 0
        count_dl = 0
        count_ul = 0
        count_dr = 0
        for i in range(1, 4):
            if last_move_row + i < 6 and last_move_column + i < 7:
                if self.board.grid[last_move_row+i][last_move_column+i] == player and urc != -1:
                    count_ur += 1
                else:
                    urc = -1
            if last_move_row - i >= 0 and last_move_column - i >= 0:
                if self.board.grid[last_move_row - i][last_move_column - i] == player and dlc != -1:
                    count_dl += 1
                else:
                    dlc = -1
            if last_move_row - i >= 0 and last_move_column + i < 7:
                if self.board.grid[last_move_row - i][last_move_column + i] == player and ulc != -1:
                    count_ul += 1
                else:
                    ulc = -1
            if last_move_row + i < 6 and last_move_column - i >= 0:
                if self.board.grid[last_move_row + i][last_move_column - i] == player and drc != -1:
                    count_dr += 1
                else:
                    drc = -1
            if count_ur + count_dl == 3:
                return True
            if count_ul + count_dr == 3:
                return True
            if count_ur == 3 or count_dl == 3:
                return True
            if count_ul == 3 or count_dr == 3:
                return True
            if count_ur < i and count_dl < i and count_ul < i and count_dr < i:
                break

        return False

    def check_draw(self):
        """
        Checks if the board is full.
        :return: True if the board is full, False otherwise.
        """
        for i in range(7):
            if self.board.grid[0][i] == 0:
                return False
        return True


