import pygame
import numpy

from path_builder import build_path

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (700, 500)


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("sinedraw")

        self.harmonics = [
                [2,2,2],
                [3,1,3],
                [-4,3,2],
                [-1,2,1]
            ]
        self.origin = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        self.running = True

    def run(self):

        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.render()

            pygame.display.flip()

    def render(self):
        self.screen.fill("#0F1A20")

        path = build_path(self.harmonics, 10, 10, self.origin)
        print(path)

        pygame.draw.circle(self.screen, "green", self.origin, 1)
        pygame.draw.lines(self.screen, "red", True, path)









if __name__ == '__main__':
    window = MainWindow()

    window.run()











