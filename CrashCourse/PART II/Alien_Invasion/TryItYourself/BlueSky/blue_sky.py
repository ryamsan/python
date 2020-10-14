import pygame, sys
from settings import Settings


class BlueSky:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Blue Sky')

    def run_prog(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    ai = BlueSky()
    ai.run_prog()