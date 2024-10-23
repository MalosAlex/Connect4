from src.ui.ui import Ui
from src.ui.gui import Gui
from src.domain.board import Board
from src.services.services import Services
from src.services.ai import Ai
from src.services.ai2 import Ai2
import pygame as pg


if __name__ == '__main__':
    ui = Gui()
    while True:
        opt = ui.start()
        if opt == '1':
            # board = Board()
            board = ui.start_game()
            ui.draw_board()
            services = Services(board)
            while True:
                opt = ui.game()
                if opt == '0':
                    break
                elif opt in ['1', '2', '3', '4', '5', '6', '7']:
                    if board.grid[0][int(opt) - 1] != 0:
                        ui.move_feedback(-2)
                        continue
                    row = services.make_move(int(opt) - 1, 1)
                    if services.check_win(1, int(opt) - 1, row):
                        ui.draw_board()
                        ui.move_feedback(1)
                        break
                    if services.check_draw():
                        ui.draw_board()
                        ui.move_feedback(0)
                        break

                    AI = Ai(5, board)
                    ai_move = AI.negamax(5, -1, int(opt) - 1)
                    # ai_move = AI.basis_AI()

                    row = services.make_move(ai_move, -1)
                    ui.draw_board()
                    if services.check_win(-1, ai_move, row):
                        ui.move_feedback(-1)
                        break
                    if services.check_draw():
                        ui.move_feedback(0)
                        break
                else:
                    ui.move_feedback(-2)
        elif opt == '2':
            ui.help()
        elif opt == '3':
            break
        else:
            print("Invalid option!")

# Still some issues with the AI, but should focus now on the GUI
# The AI is not very smart, but it's a start. I will try to improve it in the future. Thinking the main problem
# is the heuristic function.

# The AI fails when the user has 3 pieces in a row with a 0 between them and the AI has nothing.
# It should block either one of those 0's but it doesn't