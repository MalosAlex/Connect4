from unittest import TestCase
from src.domain.board import Board
from src.services.services import Services
from src.services.ai import Ai


class TestAi(TestCase):
    def setUp(self):
        self.board = Board()
        self.services = Services(self.board)
        self.ai = Ai(4, self.board)

    def test_heuristic(self):
        self.board.grid = [[-1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0]]
        self.services = Services(self.board)
        self.ai = Ai(4, self.board)
        print(self.ai.heuristic())
        self.assertEqual(self.ai.heuristic(), 20.599999999999994)

    def test_negamax(self):
        # The AI should play in column 4 to intercept the player's winning move.
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, -1, 0],
                           [-1, 0, 1, 1, 0, 1, 0]]
        self.ai = Ai(5, self.board)
        ai_move = self.ai.negamax(5, -1, 0)
        self.assertEqual(ai_move, 4)
    def test_negamax2(self):
        # The AI should play in column 1 to intercept the player's winning move.
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [-1, 0, -1, 0, 0, 0, 0],
                           [-1, 0, 1, 1, 1, 0, 1]]
        self.ai = Ai(6, self.board)
        ai_move = self.ai.negamax(6, -1, 5)
        self.assertEqual(ai_move, 1)

    def test_negamax3(self):
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 1, 1, 1, 0, 0]]
        self.ai = Ai(5, self.board)
        ai_move = self.ai.negamax(5, -1, 2)
        self.assertEqual(ai_move, 1)

    def test_win(self):
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, -1, 0, 0, 0],
                           [0, 0, 0, -1, 0, 0, 0],
                           [0, 0, 0, -1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [-1, 0, 1, 1, 0, 0, 0]]
        self.ai = Ai(5, self.board)
        self.services = Services(self.board)
        print(self.services.check_win(-1, 3, self.board.get_row_nonempty(3)))
        ai_move = self.ai.negamax(5, -1, 3)
        self.assertEqual(ai_move, 3)

    def test_7(self):
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [1, -1, 0, 0, 0, 0, 0],
                           [-1, 1, 0, 0, 0, 0, 0],
                           [-1, 1, 0, 0, 0, 0, 0],
                           [-1, 1, 1, 1, -1, 0, 0]]
        self.ai = Ai(5, self.board)
        ai_move = self.ai.negamax(5, -1, 5)
        print(ai_move)

    def test_failling_negamax(self):
        self.board.grid = [[0, 0, 0, 0, 0, 0, 0],
                           [-0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, 0, 0],
                           [-1, 0, 0, 0, 0, -1, 0],
                           [-1, 0, 0, 1, 0, 1, 0]]
        self.ai = Ai(5, self.board)
        ai_move = self.ai.negamax(5, -1, 0)
        self.assertEqual(ai_move, 2)
