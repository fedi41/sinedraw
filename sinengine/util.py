import json
import math

import numpy as np
import numpy.random
import random


#
def points_to_harmonics(points):
    points = np.array(points)
    x,y = points[:,0],points[:,1]

    z = x + 1j * y # complex

    n = len(z)
    coeffs = np.fft.fft(z)/n

    freqs = np.fft.fftfreq(n, d=1/n)

    amp = np.abs(coeffs)
    phase = np.angle(coeffs)

    harmonics = np.stack([freqs, amp, phase], axis=1)
    return harmonics


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
    h1 = np.array(h1)
    h2 = np.array(h2)

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

def shortest_angle_diff(a, b):
    diff = (b - a + np.pi) % (2 * np.pi) - np.pi
    return diff

def lerp_harmonics(h1, h2, progress):
    freq = h1[:, 0]
    amp = h1[:, 1] * (1 - progress) + h2[:, 1] * progress
    phase_diff = shortest_angle_diff(h1[:, 2], h2[:, 2])
    phase = h1[:, 2] + phase_diff * progress
    return np.stack([freq, amp, phase], axis=1)

def scale_harmonics(harmonics, scale):
    harmonics = np.array(harmonics)
    harmonics[:, 1] *= scale
    return harmonics

def top_n_harmonics(harmonics, n):
    idx = np.argsort(-harmonics[:, 1])
    return harmonics[idx[:n]]

def remove_offset(harmonics):
    harmonics[0] = [0,0,0]
    return harmonics

def move_harmonics(harmonics, vector):
    harmonics = np.array(harmonics)
    harmonics[:] += vector
    return harmonics
