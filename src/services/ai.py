from random import randint, choice
from src.services.services import Services


class Ai:
    def __init__(self, depth, board):
        self.depth = depth
        self.f_board = board
        self.board = board.clone()
        self.services = Services(self.board)
        self.best_move1 = None
        self.best_move_1 = None
        self.best_value1 = float('-inf')
        self.best_value_1 = float('inf')
        self.best_depth1 = 0
        self.best_depth_1 = 0


    def random_move(self):
        """
        Makes a random move.
        :return:
        """
        r = randint(0, 6)
        while self.board.grid[0][r] != 0:
            r = randint(0, 6)
        return r

    def negamax(self, depth, player, last_move):
        """
        The negamax algorithm.
        We first check if there is an immediate win for the player. If there is we return the score 0 or 42 if it's not
        at the first depth. If there is no immediate win we make a move for the player and check if the opponent can win
        in the next move. If he can we block him. If he can't we check if we can win in the next move and do so.
        If we can't win we choose a value based on the heuristic function.
        :param depth:
        :param player:
        :param last_move:
        :return:
        """
        if depth == 0:
            return self.heuristic()
        for i in range(7):
            if self.board.grid[0][i] == 0:
                self.services.make_move(i, player)
                # Check for an immediate win
                if self.services.check_win(player, i, self.board.get_row_nonempty(i)):
                    self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                    if depth == self.depth:
                        return i
                    return 21 + player * 21
                self.board.grid[self.board.get_row_nonempty(i)][i] = 0
        for i in range(7):
            if self.board.grid[0][i] == 0:
                self.services.make_move(i, -player)
                if self.services.check_win(-player, i, self.board.get_row_nonempty(i)):
                    self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                    if depth == self.depth:
                        return i
                    return 21 - player * 21
                self.board.grid[self.board.get_row_nonempty(i)][i] = 0


        for i in range(7):
            if self.board.grid[0][i] == 0:
                self.services.make_move(i, player)

                value = self.negamax(depth - 1, -player, i)

                # Undo the move
                self.board.grid[self.board.get_row_nonempty(i)][i] = 0

                if value > self.best_value1:
                    self.best_value1 = value
                    self.best_move1 = i

                if value < self.best_value_1:
                    self.best_value_1 = value
                    self.best_move_1 = i

                if (value == 42 or value == 0) and depth > self.depth:
                    self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                    if depth == self.depth:
                        return i
                    return value

                if value == self.best_value1 and depth > self.best_depth1:
                    self.best_depth1 = depth
                    self.best_move1 = i

                if value == self.best_value_1 and depth > self.best_depth_1:
                    self.best_depth_1 = depth
                    self.best_move_1 = i

        if depth == self.depth:
            if player == 1:
                return self.best_move1
            else:
                return self.best_move_1

        if player == 1:
            return self.best_value1
        else:
            return self.best_value_1

    def heuristic(self):
        """
        The heuristic function will return a value for the current state of the board.
        We will make winning scores 42 or 0 if the player has won.
        We will calculate the score taking into consideration the number of pieces in a row, column or diagonal.
        1 piece = 0.1 points
        2 pieces = 0.3 points
        3 pieces = 0.9 points
        We will also check that the pieces are not blocked by the opponent.
        UPDATE: We will also check now if a row or column is blocked by the opponent.
        If it is we make it a 0.1 score. instead of 0.3 or 0.9 if its blocked in both directions.
        :return: the score for this state
        """
        score = 21

        # Horizontal check

        for i in range(6):
            j = 0
            while j < 7:
                if self.board.grid[i][j] != 0:
                    # horizontal check
                    count_r = 0
                    count_r_save = 0
                    for k in range(1, 4):
                        if j + k < 7:
                            if self.board.grid[i][j + k] == self.board.grid[i][j]:
                                count_r += 1
                                count_r_save = count_r
                            else:
                                break
                    # Check if the row is blocked by the opponent on both sides
                    if j - 1 >= 0:
                        if (self.board.grid[i][j - 1] == -self.board.grid[i][j]
                                and (j + count_r + 1 >= 6
                                     or self.board.grid[i][j + count_r + 1] == -self.board.grid[i][j])):
                            count_r_save = count_r
                            count_r = 0
                    # Check if the row is blocked by the opponent on one side and the wall on the other
                    if j == 0:
                        if self.board.grid[i][j + count_r + 1] == -self.board.grid[i][j]:
                            count_r_save = count_r
                            count_r = 0
                    if count_r == 3:
                        return 21 + self.board.grid[i][j] * 21
                    if count_r == 2:
                        score += 0.9 * self.board.grid[i][j]
                    if count_r == 1:
                        score += 0.3 * self.board.grid[i][j]
                    else:
                        score += 0.1 * self.board.grid[i][j]
                    j = j + count_r_save
                j = j + 1

        # Vertical check

        for j in range(7):
            i = 0
            while i < 6:
                if self.board.grid[i][j] != 0:
                    count_u = 0
                    count_u_save = 0
                    for k in range(1, 4):
                        if i + k < 6:
                            if self.board.grid[i + k][j] == self.board.grid[i][j]:
                                count_u += 1
                                count_u_save = count_u
                            else:
                                break
                    # Check if the column is blocked by the opponent on both sides
                    if i - 1 >= 0:
                        if (self.board.grid[i - 1][j] == -self.board.grid[i][j]
                                and (i + count_u + 1 >= 5 or
                                     self.board.grid[i + count_u + 1][j] == -self.board.grid[i][j])):
                            count_u_save = count_u
                            count_u = 0
                    # Check if the column is blocked by the opponent on one side and the wall on the other
                    if i == 0:
                        if self.board.grid[i + count_u + 1][j] == -self.board.grid[i][j]:
                            count_u_save = count_u
                            count_u = 0
                    if count_u == 3:
                        return 21 + self.board.grid[i][j] * 21
                    if count_u == 2:
                        score += 0.9 * self.board.grid[i][j]
                    if count_u == 1:
                        score += 0.3 * self.board.grid[i][j]
                    i = i + count_u_save
                i = i + 1

        # Diagonal check (top-left to bottom-right)

        i = 0
        while i < 6:
            j = 0
            while j < 7:
                if self.board.grid[i][j] != 0:
                    count_ur = 0
                    count_ur_save = 0
                    for k in range(1, 4):
                        if i + k < 6 and j + k < 7:
                            if self.board.grid[i + k][j + k] == self.board.grid[i][j]:
                                count_ur += 1
                                count_ur_save = count_ur
                            else:
                                break
                    # Check if the diagonal is blocked by the opponent on both sides
                    if i - 1 >= 0 and j - 1 >= 0:
                        if (self.board.grid[i - 1][j - 1] == -self.board.grid[i][j]
                                and (i + count_ur + 1 >= 5 or j + count_ur + 1 >= 6 or
                                     self.board.grid[i + count_ur + 1][j + count_ur + 1] == -self.board.grid[i][j])):
                            count_ur_save = count_ur
                            count_ur = 0
                    # Check if the diagonal is blocked by the opponent on one side and the wall on the other
                    if i == 0 and j == 0:
                        if self.board.grid[i + count_ur + 1][j + count_ur + 1] == -self.board.grid[i][j]:
                            count_ur_save = count_ur
                            count_ur = 0
                    if count_ur == 3:
                        return 21 + self.board.grid[i][j] * 21
                    if count_ur == 2:
                        score += 0.9 * self.board.grid[i][j]
                    if count_ur == 1:
                        score += 0.3 * self.board.grid[i][j]
                    i = i + count_ur_save
                    j = j + count_ur_save
                j = j + 1
            i = i + 1

        # Diagonal check (top-right to bottom-left)

        i = 0
        while i < 6:
            j = 0
            while j < 7:
                if self.board.grid[i][j] != 0:
                    count_ul = 0
                    count_ul_save = 0
                    for k in range(1, 4):
                        if i + k < 6 and j - k >= 0:
                            if self.board.grid[i + k][j - k] == self.board.grid[i][j]:
                                count_ul += 1
                                count_ul_save = count_ul
                            else:
                                break
                    # Check if the diagonal is blocked by the opponent on both sides
                    if i - 1 >= 0 and j + 1 < 7:
                        if (self.board.grid[i - 1][j + 1] == -self.board.grid[i][j]
                                and (i + count_ul + 1 >= 6 or j - count_ul - 1 < 0 or
                                     self.board.grid[i + count_ul + 1][j - count_ul - 1] == -self.board.grid[i][j])):
                            count_ul_save = count_ul
                            count_ul = 0
                    # Check if the diagonal is blocked by the opponent on one side and the wall on the other
                    if i == 0 and j == 6:
                        if self.board.grid[i + count_ul + 1][j - count_ul - 1] == -self.board.grid[i][j]:
                            count_ul_save = count_ul
                            count_ul = 0

                    if count_ul == 3:
                        return 21 + self.board.grid[i][j] * 21
                    if count_ul == 2:
                        score += 0.9 * self.board.grid[i][j]
                    if count_ul == 1:
                        score += 0.3 * self.board.grid[i][j]
                    i = i + count_ul_save
                    j = j - count_ul_save
                j = j + 1
            i = i + 1

        return score

    def basis_AI(self):
        """
        The AI will check if the opponent can win in the next move and block him.
        If the opponent can't win, it will check if it can win in the next move and do so.
        If it can't win, it will make a random move.
        :return: None
        """
        # Check if the opponent can win
        for i in range(7):
            if self.board.grid[0][i] == 0:
                self.services.make_move(i, -1)
                if self.services.check_win(-1, i, self.board.get_row_nonempty(i)):
                    self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                    return i
                self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                self.services.make_move(i, 1)
                if self.services.check_win(1, i, self.board.get_row_nonempty(i)):
                    self.board.grid[self.board.get_row_nonempty(i)][i] = 0
                    return i
                self.board.grid[self.board.get_row_nonempty(i)][i] = 0
        return self.random_move()







