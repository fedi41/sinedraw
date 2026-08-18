import pygame

from core.shapes import HarmonicShape, RenderStyle, MorphShape, StyledShape
from harmonics import *
from core.renderer.pygame_renderer import PygameRenderer

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (1500, 900)


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("sinedraw")

        self.origin = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.running = True
        self.renderer = PygameRenderer(self.screen)
        self.t = 0


        self.shape = StyledShape(MorphShape(
            harmonics_star, harmonics_8_scaled
        ),
            RenderStyle(offset=self.origin, scale=100)
        )

        self.shape.shape.set_progress(0)



    def run(self):

        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()

            pygame.display.flip()

    def update(self):


        self.t += 0.0005
        if self.t > 1: self.t = 1
        self.shape.shape.set_progress(self.t)


        # self.test_sprite.shapes[0].shape.top_n(round(self.t))


    def render(self):
        self.screen.fill("#0F1A20")

        # print(self.test_sprite.render(200, 100,self.origin))
        self.renderer.renderShape(self.shape)
        pygame.draw.circle(self.screen, "green", self.origin, 1)




if __name__ == '__main__':
    window = MainWindow()
    window.run()