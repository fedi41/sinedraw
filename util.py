import math

import numpy as np
import numpy.random


def random_shift(harmonics, t):
    shift = numpy.zeros((len(harmonics), 3))
    shift[:, 1] = math.sin(t)/1000
    shift[:, 2] = math.sin(t/2)/100
    return np.array(harmonics) + shift

import random

def random_harmonics(n=10, max_amp=50):
    return [
        [random.randint(-8, 8), random.uniform(1, max_amp), random.uniform(0, 2 * math.pi)]
        for _ in range(n)
    ]