import numpy as np

from core.fft import points_to_harmonics
from core.path_builder import build_path

harmonics_square = [
    [-15, 0.0044, 0],
    [-11, 0.0083, 0],
    [-7,  0.0204, 0],
    [-3,  0.1111, 0],
    [1,   1.0000, 0],
    [5,   0.0400, 0],
    [9,   0.0123, 0],
    [13,  0.0059, 0],
]

harmonics_spiral = [
    [1,1  ,0],
    [9,0.06,0]
]

harmonics_star = [
    [1, 0.60, 0],
    [-3, 0.20, 0],
    [5, 0.10, 0],
    [6, 0.30, 0],
]


class HarmonicShape:
    def __init__(self, harmonics):
        self.harmonics = np.array(harmonics)  # [freq, amp, phase]

    @classmethod
    def from_points(cls, points):
        return cls(points_to_harmonics(points))

    def top_n(self, n):
        idx = np.argsort(-self.harmonics[:, 1])
        return HarmonicShape(self.harmonics[idx[:n]])

    def render(self, resolution=200, scale=1, origin=(0, 0)):
        return build_path(self.harmonics, resolution, scale, origin)

class RenderStyle:
    def __init__(self, color="#ffffff", width=2):
        self.color = color
        self.width = width

class StyledShape:
    def __init__(self, shape:HarmonicShape, style:RenderStyle):
        self.shape = shape
        self.style = style
    def render(self, resolution=200, scale=1, origin=(0,0)):
        return self.shape.render(resolution, scale, origin)

class HarmonicSprite:
    def __init__(self):
        self.shapes:list[StyledShape] = []

    def add(self, shape: HarmonicShape, style: RenderStyle = RenderStyle()):
        self.shapes.append(StyledShape(shape, style))
        return self

    def render(self, resolution=200, scale=1, origin=(0, 0)):
        return [
            (s.render(resolution, scale, origin), s.style)
            for s in self.shapes
        ]



