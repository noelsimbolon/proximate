import math

# dvdBy means divide by either x axis or y axis.
# dvdBy = 0 , represent divide by x
# dvdBy = 1, represent divide by y
def dnq(vectors, dimension, dvdBy=0):
    if (len(vectors) > 3): # recurence

        # sort vectors
        sorted_vectors = quickSort(vectors, dvdBy)

        # find index to divide
        divideAt = len(sorted_vectors) // 2

        # split vectors
        vectors_left = sorted_vectors[:divideAt]
        vectors_right = sorted_vectors[divideAt:]

        # recurence
        closest_left, dist_left, count_left = dnq(vectors_left, dimension, (dvdBy+1)%(dimension-1))
        closest_right, dist_right, count_right = dnq(vectors_right, dimension, (dvdBy+1)%(dimension-1))

        # find minimum
        closest_vector, min_dist = (closest_left,dist_left) if dist_left < dist_right else (closest_right,dist_right)

        # find if there were nearer points separated by the strip
        count_gray = 0
        for i in range(len(sorted_vectors)):
            for j in range(i+1, len(sorted_vectors)):
                for k in range(dimension):
                    if abs(sorted_vectors[i][k] - sorted_vectors[j][k]) > min_dist:
                        continue
                else :
                    temp_dist = distance((sorted_vectors[i], sorted_vectors[j]))
                    count_gray += 1
                    if (temp_dist < min_dist):
                        closest_vector, min_dist = (sorted_vectors[i], sorted_vectors[j]), temp_dist

        # return
        return closest_vector, min_dist, count_left+count_right+count_gray

    elif (len(vectors) == 3): # basis 1
        vect_temp1, dist1 = vectors[:2], distance(vectors[:2])
        vect_temp2, dist2 = vectors[1:3], distance(vectors[1:3])
        vect_temp3, dist3 = (vectors[0],vectors[2]), distance((vectors[0],vectors[2]))

        min_dist_temp = min(dist1, dist2, dist3)

        if min_dist_temp == dist1:
            return vect_temp1, dist1, 3
        elif min_dist_temp == dist2:
            return vect_temp2, dist2, 3
        else:
            return vect_temp3, dist3, 3

    else : # basis 2
        # find distance between 2 vectors
        dist = distance(vectors) 

        # return the two vectors and distance between them
        return vectors, dist, 1

# distance of two vector
def distance(vectors):
    point1, point2 = vectors
    sumOfSquaredDelta = 0;
    for i in range(len(point1)):
        delta =  point1[i]-point2[i]
        squared = delta**2
        sumOfSquaredDelta += squared
    distance = math.sqrt(sumOfSquaredDelta)
    return distance

def quickSort(arr, by):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2][by]

    # create array with all elements smaller than pivot
    left = [x for x in arr if x[by] < pivot]

    # create array consists only pivot
    middle = [x for x in arr if x[by] == pivot]

    # create array with all elements greater than pivot
    right = [x for x in arr if x[by] > pivot]

    sort_left = quickSort(left, by)
    sort_right = quickSort(right, by)

    return sort_left + middle + sort_right