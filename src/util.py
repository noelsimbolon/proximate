import math
import numpy as np


def euclidean_distance(first_point: np.ndarray[float], second_point: np.ndarray[float]) -> float:
    """
    :param second_point:
    :param first_point:
    :return: the Euclidean distance between two vectors.
    """
    return math.sqrt(sum([(first_point[i] - second_point[i]) ** 2 for i in range(len(first_point))]))


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
