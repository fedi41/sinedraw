from core.shapes import RenderStyle, HarmonicShape
from core.sprite import Sprite


class PreviewSprite(Sprite):
    def __init__(self):
        super().__init__()


        self.render_style = RenderStyle("white", 2)

        self.shapes = [
            HarmonicShape([])
        ]

    def modify_last_shape(self, points, max_freq_count=20):
        self.shapes[-1] = HarmonicShape.from_points(points).top_n(max_freq_count)


    def new_shape(self):
        self.shapes.append(HarmonicShape([]))