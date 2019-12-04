class Settings(object):
    def __init__(self):
        self.button_size = 100
        self.button_space = 10
        self.screen_size = (self.button_size * 4 + self.button_space * 5,
                            self.button_size * 4 + self.button_space * 5)

        self.background_color = (0, 0, 0)
        self.button_color = (255, 255, 255)

        self.font_size = 72
