import pygame


class Block(object):
    def __init__(self, settings, screen, data):
        self.settings = settings
        self.screen = screen
        self.data = data

        self.font = pygame.font.Font(None, self.settings.font_size)

    def draw_button(self):
        for i in range(4):
            for j in range(4):
                rect = (i * self.settings.button_size + (i + 1) * self.settings.button_space,
                        j * self.settings.button_size + (j + 1) * self.settings.button_space,
                        self.settings.button_size, self.settings.button_size)
                pygame.draw.rect(self.screen, self.settings.button_color, rect)
                if self.data.numbers[j][i]:
                    number_image = self.font.render(str(self.data.numbers[j][i]),
                                                    True, self.settings.background_color)
                    number_rect = number_image.get_rect()
                    number_rect.center = (rect[0] + rect[2] / 2, rect[1] + rect[3] / 2)
                    self.screen.blit(number_image, number_rect)
