import math

import numpy as np


def euclidean_distance(first_point: np.ndarray[float], second_point: np.ndarray[float]) -> float:
    """
    :param second_point: a numpy array of floats representing a single point
    :param first_point: a numpy array of floats representing a single point
    :return: the Euclidean distance between two points.
    """
    return math.sqrt(sum([(first_point[i] - second_point[i]) ** 2 for i in range(len(first_point))]))


def quick_sort(points: np.ndarray[np.ndarray[float]], divide_by: int) -> np.ndarray[np.ndarray[float]]:
    """
    Performs quick sort to an array of points
    :param points: a numpy array of points
    :param divide_by: the index of column to sort by
    :return: points sorted by a certain column (in this case, columns represent axes)
    """

    if len(points) <= 1:
        return points

    pivot = points[len(points) // 2][divide_by]

    # Create array with all elements smaller than pivot
    left = points[points[:, divide_by] < pivot]

    # Create array consists only pivot
    middle = points[points[:, divide_by] == pivot]

    # Create array with all elements greater than pivot
    right = points[points[:, divide_by] > pivot]

    return np.concatenate((quick_sort(left, divide_by), middle, quick_sort(right, divide_by)))


def validate_number_of_dimensions(d: str) -> bool:
    """
    Validates the number of dimensions
    :return: whether the number of points is >= 1
    """
    try:
        if int(d) >= 1:
            return True
    except ValueError:
        return False

    return False


def validate_number_of_points(n: str) -> bool:
    """
    Validates the number of points
    :return: whether the number of points is >= 2
    """
    try:
        if int(n) >= 2:
            return True
    except ValueError:
        return False

    return False
