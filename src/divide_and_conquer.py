import math


# divide_by means divide by either x-axis or y-axis.
# divide_by = 0 , represent divide by x
# divide_by = 1, represent divide by y
def find_closest_pair_dnc(vectors, dimension, divide_by=0):
    if len(vectors) > 3:  # recurrence

        # sort vectors
        sorted_vectors = quick_sort(vectors, divide_by)

        # find index to divide
        divide_at = len(sorted_vectors) // 2

        # split vectors
        vectors_left = sorted_vectors[:divide_at]
        vectors_right = sorted_vectors[divide_at:]

        # recurrence
        closest_left, dist_left, count_left = find_closest_pair_dnc(vectors_left, dimension,
                                                                    (divide_by + 1) %
                                                                    (dimension - 1 if dimension > 1 else dimension))
        closest_right, dist_right, count_right = find_closest_pair_dnc(vectors_right, dimension,
                                                                       (divide_by + 1) %
                                                                       (dimension - 1 if dimension > 1 else dimension))

        # find minimum
        closest_vector, min_dist = (closest_left, dist_left) if dist_left < dist_right else (closest_right, dist_right)

        # find if there were nearer points separated by the strip
        count_gray = 0
        for i in range(len(sorted_vectors)):
            for j in range(i + 1, len(sorted_vectors)):
                check_further = True
                for k in range(dimension):
                    if abs(sorted_vectors[i][k] - sorted_vectors[j][k]) > min_dist:
                        check_further = False
                        continue
                if check_further:
                    temp_dist = euclidean_distance((sorted_vectors[i], sorted_vectors[j]))
                    count_gray += 1
                    if temp_dist < min_dist:
                        closest_vector, min_dist = (sorted_vectors[i], sorted_vectors[j]), temp_dist

        # return
        return closest_vector, min_dist, count_left + count_right + count_gray

    elif len(vectors) == 3:  # basis 1
        vect_temp1, dist1 = vectors[:2], euclidean_distance(vectors[:2])
        vect_temp2, dist2 = vectors[1:3], euclidean_distance(vectors[1:3])
        vect_temp3, dist3 = (vectors[0], vectors[2]), euclidean_distance((vectors[0], vectors[2]))

        min_dist_temp = min(dist1, dist2, dist3)

        if min_dist_temp == dist1:
            return vect_temp1, dist1, 3
        elif min_dist_temp == dist2:
            return vect_temp2, dist2, 3
        else:
            return vect_temp3, dist3, 3

    else:  # basis 2
        # find distance between 2 vectors
        dist = euclidean_distance(vectors)

        # return the two vectors and distance between them
        return vectors, dist, 1


# distance of two vector
def euclidean_distance(vectors):
    first_point = vectors[0]
    second_point = vectors[1]
    sum_of_squared_delta = 0

    for i in range(len(first_point)):
        delta = first_point[i] - second_point[i]
        squared = delta ** 2
        sum_of_squared_delta += squared

    distance = math.sqrt(sum_of_squared_delta)

    return distance


def quick_sort(arr, by):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2][by]

    # create array with all elements smaller than pivot
    left = [x for x in arr if x[by] < pivot]

    # create array consists only pivot
    middle = [x for x in arr if x[by] == pivot]

    # create array with all elements greater than pivot
    right = [x for x in arr if x[by] > pivot]

    sort_left = quick_sort(left, by)
    sort_right = quick_sort(right, by)

    return sort_left + middle + sort_right
