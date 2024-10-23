from src.services.services import Services
from random import randint


class Position:
    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.moves = 0
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]

    def nbMoves(self):
        return self.moves

    def canPlay(self, col):
        return self.board[0][col] == 0

    def isWinningMove(self, col):
        row = self.get_row_nonempty(col)
        player = self.board[row][col]

        # Check horizontal
        if self.check_line(row, col, 0, 1, player):
            return True

        # Check vertical
        if self.check_line(row, col, 1, 0, player):
            return True

        # Check diagonal (top-left to bottom-right)
        if self.check_line(row, col, 1, 1, player):
            return True

        # Check diagonal (top-right to bottom-left)
        if self.check_line(row, col, 1, -1, player):
            return True

        return False

    def get_row_nonempty(self, col):
        for row in range(self.HEIGHT - 1, -1, -1):
            if self.board[row][col] == 0:
                return row
        return 0

    def check_line(self, row, col, dr, dc, player):
        count = 1
        for i in range(1, 4):
            r = row + i * dr
            c = col + i * dc
            if 0 <= r < self.HEIGHT and 0 <= c < self.WIDTH and self.board[r][c] == player:
                count += 1
            else:
                break

        for i in range(1, 4):
            r = row - i * dr
            c = col - i * dc
            if 0 <= r < self.HEIGHT and 0 <= c < self.WIDTH and self.board[r][c] == player:
                count += 1
            else:
                break

        return count >= 4

    def play(self, col):
        row = self.get_row_nonempty(col)
        self.board[row][col] = 1 if self.moves % 2 == 0 else -1
        self.moves += 1


class Ai2:
    def __init__(self, depth, board):
        self.depth = depth
        self.f_board = board
        self.board = board.clone()
        self.services = Services(self.board)
        self.best_move1 = None
        self.best_move_1 = None
        self.best_value1 = self.heuristic()
        self.best_value_1 = 42 - self.best_value1

    def random_move(self):
        r = randint(0, 6)
        while self.board.grid[0][r] != 0:
            r = randint(0, 6)
        return r

    def negamax(self, depth, alpha, beta, last_move):
        if depth == 0:
            return self.heuristic()

        if last_move != -1:
            if self.services.check_win(-1, last_move, self.board.get_row_nonempty(last_move)):
                return (Position.WIDTH * Position.HEIGHT + 1 - self.board.nbMoves()) / 2

        for x in range(Position.WIDTH):
            if self.board.canPlay(x):
                print(x)
                self.board.play(x)
                if self.services.check_win(1, x, self.board.get_row_nonempty(x)):
                    print(self.board)
                    self.board.grid[self.board.get_row_nonempty(x)][x] = 0
                    return (Position.WIDTH * Position.HEIGHT + 1 - self.board.nbMoves()) / 2

                score = -self.negamax(depth - 1, -beta, -alpha, x)

                # no need to have good precision for score better than beta (opponent's score worse than -beta)
                # no need to check for score worse than alpha (opponent's score worse better than -alpha)
                if score >= beta:
                    self.board.grid[self.board.get_row_nonempty(x)][x] = 0
                    return score  # prune the exploration if we find a possible move better than what we were looking for.

                if score > alpha:
                    alpha = score  # reduce the [alpha;beta] window for next exploration, as we only
                    # need to search for a position that is better than the best so far.

                self.board.grid[self.board.get_row_nonempty(x)][x] = 0

        return alpha

    def heuristic(self):
        score = 0

        for i in range(6):
            for j in range(7):
                if self.board.grid[i][j] != 0:
                    # Check horizontal
                    count = 1
                    for k in range(1, 4):
                        if j + k < 7 and self.board.grid[i][j + k] == self.board.grid[i][j]:
                            count += 1
                        else:
                            break

                    # Update score based on count
                    if count >= 4:
                        return 42 if self.board.grid[i][j] == 1 else 0
                    score += count * 0.1

                    # Check vertical
                    count = 1
                    for k in range(1, 4):
                        if i + k < 6 and self.board.grid[i + k][j] == self.board.grid[i][j]:
                            count += 1
                        else:
                            break

                    # Update score based on count
                    if count >= 4:
                        return 42 if self.board.grid[i][j] == 1 else 0
                    score += count * 0.1

                    # Check diagonal (top-left to bottom-right)
                    count = 1
                    for k in range(1, 4):
                        if i + k < 6 and j + k < 7 and self.board.grid[i + k][j + k] == self.board.grid[i][j]:
                            count += 1
                        else:
                            break

                    # Update score based on count
                    if count >= 4:
                        return 42 if self.board.grid[i][j] == 1 else 0
                    score += count * 0.1

                    # Check diagonal (top-right to bottom-left)
                    count = 1
                    for k in range(1, 4):
                        if i + k < 6 and j - k >= 0 and self.board.grid[i + k][j - k] == self.board.grid[i][j]:
                            count += 1
                        else:
                            break

                    # Update score based on count
                    if count >= 4:
                        return 42 if self.board.grid[i][j] == 1 else 0
                    score += count * 0.1

        # Ensure the score is within the range [0, 42]
        return max(0, min(score, 42))
