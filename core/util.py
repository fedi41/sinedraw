import math

import numpy as np
import numpy.random
import random


def random_shift(harmonics, t):
    shift = numpy.zeros((len(harmonics), 3))
    shift[:, 1] = math.sin(t)/1000
    shift[:, 2] = math.sin(t/2)/100
    return np.array(harmonics) + shift


def random_harmonics(n=10, max_amp=50):
    return [
        [random.randint(-8, 8), random.uniform(1, max_amp), random.uniform(0, 2 * math.pi)]
        for _ in range(n)
    ]

def align_harmonics(h1, h2):
    freqs1 = set(h1[:, 0])
    freqs2 = set(h2[:, 0])
    all_freqs = sorted(freqs1 | freqs2)

    def build_full(h, freqs):
        lookup = {row[0]: row for row in h}
        result = []
        for f in freqs:
            if f in lookup:
                result.append(lookup[f])
            else:
                result.append([f, 0, 0])  # amp=0, phase=0 -> keine Wirkung
        return np.array(result)

    return build_full(h1, all_freqs), build_full(h2, all_freqs)

def lerp_harmonics(h1, h2, progress):
    # amp und phase linear interpolieren, freq bleibt gleich (ist ja jetzt identisch)
    freq = h1[:, 0]
    amp = h1[:, 1] * (1 - progress) + h2[:, 1] * progress
    phase = h1[:, 2] * (1 - progress) + h2[:, 2] * progress
    return np.stack([freq, amp, phase], axis=1)