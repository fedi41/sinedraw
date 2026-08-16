import pygame

from core.harmonics import harmonics_star, HarmonicSprite, HarmonicShape, RenderStyle
from renderer.pygame_renderer.renderer import PygameRenderer

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = (1500, 900)


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("sinedraw")

        self.origin = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.running = True
        self.renderer = PygameRenderer(self.screen)
        self.t = 0

        self.test_sprite = HarmonicSprite()
        self.test_sprite.add(HarmonicShape(harmonics_star), RenderStyle("red", 5))



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

        self.test_sprite.shapes[0].shape.top_n(round(self.t))


    def render(self):
        self.screen.fill("#0F1A20")

        # print(self.test_sprite.render(200, 100,self.origin))
        self.renderer.draw(self.test_sprite, 100, 200,self.origin)

        pygame.draw.circle(self.screen, "green", self.origin, 1)





window = MainWindow()
window.run()



