import math


# divide_by means divide by either x-axis or y-axis.
# divide_by = 0 , represent divide by x
# divide_by = 1, represent divide by y
def dnq(vectors, dimension, divide_by=0):
    if len(vectors) > 3:  # recurrence

        # sort vectors
        sorted_vectors = sort(vectors, divide_by)

        # find index to divide
        divide_at = len(sorted_vectors) // 2

        # split vectors
        vectors_left = sorted_vectors[:divide_at]
        vectors_right = sorted_vectors[divide_at:]

        # recurrence
        closest_left, dist_left, count_left = dnq(vectors_left, dimension, (divide_by + 1) % (dimension - 1))
        closest_right, dist_right, count_right = dnq(vectors_right, dimension, (divide_by + 1) % (dimension - 1))

        # find minimum
        closest_vector, min_dist = (closest_left, dist_left) if dist_left < dist_right else (closest_right, dist_right)

        # counter if there is point one point in left and one point in right that is nearer
        base_left = vectors_left[-1][divide_by]
        base_right = vectors_right[0][divide_by]

        base_avg = (base_left + base_right) / 2

        border_left = base_avg - min_dist
        border_right = base_avg + min_dist

        # collect all points within border
        count_gray = 0
        vectors_gray = []

        # collect from left side
        i = 1
        while i <= len(vectors_left) and vectors_left[-i][divide_by] >= border_left:
            vectors_gray.append(vectors_left[-i])
            i += 1

        # collect from right side
        j = 0
        while j < len(vectors_right) and vectors_right[j][divide_by] <= border_right:
            vectors_gray.append(vectors_right[j])
            j += 1

        # sort vectors_gray
        vectors_gray_sorted = sort(vectors_gray, (divide_by + 1) % (dimension))

        # flag variable to break
        break_in_j = False
        for i in range(len(vectors_gray_sorted)):
            for j in range(i + 1, len(vectors_gray_sorted)):
                for k in range(dimension):
                    if abs(vectors_gray_sorted[i][k] - vectors_gray_sorted[j][k]) > min_dist:
                        break_in_j = True
                        break
                if break_in_j:
                    break_in_j = False
                    break
                else:
                    temp_dist = euclidean_distance((vectors_gray_sorted[i], vectors_gray_sorted[j]))
                    count_gray += 1
                    if temp_dist < min_dist:
                        closest_vector, min_dist = (vectors_gray_sorted[i], vectors_gray_sorted[j]), temp_dist

        # return
        return closest_vector, min_dist, count_left + count_right + count_gray

        # repeat
        # sort by x
        # divide by x
        # sort by y
        # divide by y

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


# by = 0, sort by x-axis
# by = 1, sort by y-axis
def sort(vectors, by):
    key_func = lambda vector: vector[by]
    sorted_vectors = sorted(vectors, key=key_func)
    return sorted_vectors


# euclidean distance of two vector
def euclidean_distance(vectors):

    point1, point2 = vectors
    sumOfSquaredDelta = 0

    for i in range(len(point1)):
        delta = point1[i] - point2[i]
        squared = delta ** 2
        sumOfSquaredDelta += squared

    distance = math.sqrt(sumOfSquaredDelta)

    return distance
