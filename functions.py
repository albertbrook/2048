import pygame


class Functions(object):
    def __init__(self, settings, screen, block, data):
        self.settings = settings
        self.screen = screen
        self.block = block
        self.data = data

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.data.start_game()
                elif event.key == pygame.K_RIGHT:
                    return self.data.right_move()
                elif event.key == pygame.K_LEFT:
                    return self.data.left_move()
                elif event.key == pygame.K_DOWN:
                    return self.data.down_move()
                elif event.key == pygame.K_UP:
                    return self.data.up_move()

    def draw_screen(self):
        self.screen.fill(self.settings.background_color)
        self.block.draw_button()
        pygame.display.flip()
