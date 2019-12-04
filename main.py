import pygame
from settings import Settings
from functions import Functions
from block import Block
from data import Data


class Game(object):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.data = Data()
        self.block = Block(self.settings, self.screen, self.data)
        self.functions = Functions(self.settings, self.screen, self.block, self.data)

    def start(self):
        while True:
            if self.functions.check_event():
                self.data.random_display()
            self.functions.draw_screen()


if __name__ == '__main__':
    game = Game()
    game.start()
