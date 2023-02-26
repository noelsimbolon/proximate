from typing import Tuple

import numpy as np

import brute_force as bf
import util


# divide_by means divide by either x-axis or y-axis.
# divide_by = 0 , represent divide by x
# divide_by = 1, represent divide by y
def find_closest_pair_dnc(points: np.ndarray[np.ndarray[float]], dimension: int, divide_by: int = 0) -> \
        Tuple[Tuple[np.ndarray[float], np.ndarray[float]], float, int]:
    """
    Finds the closest pair of points using divide-and-conquer algorithm
    :param points: a numpy array of points
    :param dimension: the number of dimensions of the points
    :param divide_by: the index of column to divide-and-conquer by
    :return: a tuple: (the closest pair of points, its distance, number of Euclidean distance operations)
    """

    if len(points) > 3:  # recurrence

        # sort points
        sorted_points = util.quick_sort(points, divide_by)

        # find index to divide
        divide_at = len(sorted_points) // 2

        # split points
        points_left = sorted_points[:divide_at]
        points_right = sorted_points[divide_at:]

        # recurrence
        closest_left, dist_left, count_left = find_closest_pair_dnc(points_left, dimension,
                                                                    (divide_by + 1) %
                                                                    (dimension - 1 if dimension > 1 else dimension))
        closest_right, dist_right, count_right = find_closest_pair_dnc(points_right, dimension,
                                                                       (divide_by + 1) %
                                                                       (dimension - 1 if dimension > 1 else dimension))

        # find minimum
        closest_vector, min_dist = (closest_left, dist_left) if dist_left < dist_right else (closest_right, dist_right)

        # find if there were nearer points separated by the strip
        count_gray = 0
        for i in range(len(sorted_points)):
            for j in range(i + 1, len(sorted_points)):

                check_further = True
                for k in range(dimension):

                    if abs(sorted_points[i][k] - sorted_points[j][k]) > min_dist:
                        check_further = False
                        continue

                if check_further:
                    temp_dist = util.euclidean_distance(sorted_points[i], sorted_points[j])
                    count_gray += 1

                    if temp_dist < min_dist:
                        closest_vector, min_dist = (sorted_points[i], sorted_points[j]), temp_dist

        # return
        return closest_vector, min_dist, count_left + count_right + count_gray

    elif len(points) == 3:  # first basis
        return bf.find_closest_pair_bf(points)

    else:  # second basis
        # find distance between 2 points
        dist = util.euclidean_distance(points[0], points[1])

        # return the two points and distance between them
        return (points[0], points[1]), dist, 1
