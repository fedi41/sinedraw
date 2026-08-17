import core.harmonics
from core.harmonics import HarmonicSprite, HarmonicShape, Shape, RenderStyle


class PreviewSprite(HarmonicSprite):
    def __init__(self):
        super().__init__()


        self.render_style = RenderStyle("white", 2)

        self.shapes = [
            Shape(HarmonicShape([]), self.render_style)
        ]

    def modify_last_shape(self, points, max_freq_count=20):
        self.shapes[-1] = Shape(HarmonicShape.from_points(points).top_n(max_freq_count), self.render_style)


    def new_shape(self):
        self.shapes.append(Shape(HarmonicShape([]), self.render_style))