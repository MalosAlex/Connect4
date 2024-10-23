import pygame as pg
from pygame.locals import QUIT

from src.domain.board import Board


class Gui:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((700, 800))
        pg.display.set_caption("Connect-4")
        self.clock = pg.time.Clock()
        self.board = None

    def start(self):
        """
        Displays the menu and returns the option selected by the user.
        :return:
        """
        font = pg.font.Font(None, 36)

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return

            self.screen.fill((255, 255, 255))

            text = font.render("Hello! Welcome to Connect-4!", True, (0, 0, 0))
            self.screen.blit(text, (50, 50))

            text = font.render("Please select an action:", True, (0, 0, 0))
            self.screen.blit(text, (50, 100))

            text = font.render("1. Begin the game", True, (0, 0, 0))
            self.screen.blit(text, (50, 150))

            text = font.render("2. Help", True, (0, 0, 0))
            self.screen.blit(text, (50, 200))

            text = font.render("3. Exit", True, (0, 0, 0))
            self.screen.blit(text, (50, 250))

            pg.display.flip()
            self.clock.tick(30)

            opt = None
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        opt = '1'
                    elif event.key == pg.K_2:
                        opt = '2'
                    elif event.key == pg.K_3:
                        opt = '3'

            if opt:
                return opt

    def start_game(self):
        """
        Creates a new board for the game and returns it
        :return:
        """
        self.board = Board()
        return self.board

    def game(self):
        """
        Displays the game and returns the option selected by the user.
        :return:
        """
        font = pg.font.Font(None, 36)

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return

            self.screen.fill((255, 255, 255))

            text = font.render("Please insert a position: 1-7 or 0 to exit and finish the game.", True, (0, 0, 0))
            self.screen.blit(text, (50, 50))

            self.draw_board()

            pg.display.flip()
            self.clock.tick(30)

            opt = None
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN and pg.K_0:
                    opt = str(event.key - pg.K_0)

            if opt:
                return str(opt)

    def help(self):
        """
        Displays the help menu.
        :return:
        """
        font = pg.font.Font(None, 30)

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    return

            self.screen.fill((255, 255, 255))

            text = font.render("This is a game of Connect-4.", True, (0, 0, 0))
            self.screen.blit(text, (50, 50))

            text = font.render("The game is played on a 6x7 board.", True, (0, 0, 0))
            self.screen.blit(text, (50, 100))

            text = font.render("The game is played in two, and the players take turns.", True, (0, 0, 0))
            self.screen.blit(text, (50, 150))

            text = font.render("The players have to choose a column to insert their piece.", True, (0, 0, 0))
            self.screen.blit(text, (50, 200))

            text = font.render("The first player to get 4 pieces in a row, column, or diagonal wins.", True, (0, 0, 0))
            self.screen.blit(text, (50, 250))

            text = font.render("Press enter to return to the menu.", True, (0, 0, 0))
            self.screen.blit(text, (50, 300))

            pg.display.flip()
            self.clock.tick(30)

    def draw_board(self):
        """
        Draws the board on the screen.
        :return:
        """
        for row in range(6):
            for column in range(7):
                pg.draw.rect(self.screen, (21, 93, 237), (column * 100, row * 100 + 100, 100, 100))
                pg.draw.circle(self.screen, (250, 251, 252), (column * 100 + 50, row * 100 + 150), 40)
                if self.board.grid[row][column] == 1:
                    pg.draw.circle(self.screen, (255, 0, 0), (column * 100 + 50, row * 100 + 150), 40)
                elif self.board.grid[row][column] == -1:
                    pg.draw.circle(self.screen, (255, 255, 0), (column * 100 + 50, row * 100 + 150), 40)

        pg.display.flip()
        self.clock.tick(30)

    def move_feedback(self, rez):
        """
        Displays the feedback for the move.
        :param rez:
        :return:
        """
        font = pg.font.Font(None, 36)
        if rez == 0:
            text = font.render("It's a draw! Press enter to continue", True, (0, 0, 0))
        elif rez == 1:
            text = font.render("You won! Press enter to continue", True, (0, 0, 0))
        elif rez == -1:
            text = font.render("The computer won! Press enter to continue", True, (0, 0, 0))
        else:
            text = font.render("Invalid move! Press enter to continue", True, (0, 0, 0))

        while True:
            self.screen.blit(text, (50, 750))
            pg.display.flip()
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    return
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    return



