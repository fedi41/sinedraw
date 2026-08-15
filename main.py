import math

import numpy as np
import pygame
import numpy

from harmonics import harmonics_square, harmonics_spiral, harmonics_star
from path_builder import build_path, build_path_np
from util import random_shift, random_harmonics

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (1500, 900)


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("sinedraw")

        self.harmonics = np.array(harmonics_square) # random_harmonics(100,1)

        self.origin = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        self.running = True

        self.t = 0

    def run(self):

        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()

            pygame.display.flip()

    def update(self):


        self.t += 0.001


        # self.harmonics = random_shift(self.harmonics, self.t)


    def render(self):
        self.screen.fill("#0F1A20")

        path = build_path_np(self.harmonics*math.sin(self.t*10), 300, 200, self.origin)
        print(path)

        pygame.draw.circle(self.screen, "green", self.origin, 1)

        # pygame.draw.polygon(self.screen, "white", path)
        pygame.draw.lines(self.screen, "red", True, path, 5)









if __name__ == '__main__':
    window = MainWindow()

    window.run()











