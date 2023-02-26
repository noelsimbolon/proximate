from typing import Tuple

import numpy as np

import util


def find_closest_pair_bf(points: np.ndarray[np.ndarray[float]]) -> \
        Tuple[Tuple[np.ndarray[float], np.ndarray[float]], float, int]:
    """
    Finds the closest pair of points using brute-force algorithm
    :param points: a numpy array of points
    :return: a tuple: (the closest pair of points, its distance, number of Euclidean distance operations)
    """

    distance_count = 0
    min_dist = float('inf')
    closest_pair = None
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):

            dist = util.euclidean_distance(points[i], points[j])
            distance_count += 1

            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return closest_pair, min_dist, distance_count
