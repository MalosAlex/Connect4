from src.domain.board import Board


class Ui:
    def __init__(self):
        self.board = None

    def start(self):
        print("Hello! Welcome to Connect-4!")
        print("Please select an action:")
        print("1.Begin the game")
        print("2.Help")
        print("3.Exit")
        opt = input(">")
        return opt

    def game(self):
        print("Please insert a position: 1-7 or 0 to exit and finish the game.")
        opt = input(">")
        return opt

    def start_game(self):
        self.board = Board()
        return self.board

    def draw_board(self):
        print(self.board)

    def help(self):
        b = Board()
        print("This is a game of Connect-4.")
        print("The game is played on a 6x7 board.")
        print("The game is played in two and the players take turns.")
        print("The players have to choose a column to insert their piece.")
        print("The first player to get 4 pieces in a row column or diagonal wins.")
        print("Press enter to return to the menu.")
        input(">")

    def move_feedback(self, result):
        if result == 1:
            print("You won!")
        elif result == -1:
            print("You lost!")
        elif result == 0:
            print("It's a draw!")
        else:
            print("Invalid move!")
