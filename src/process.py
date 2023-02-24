import math

# dvdBy means divide by either x axis or y axis.
# dvdBy = 0 , represent divide by x
# dvdBy = 1, represent divide by y
def dnq(vectors, dimension, dvdBy=0):
    if (len(vectors) > 2): # recurence

        # sort vectors
        sorted_vectors = sort(vectors, dvdBy)

        # find index to divide
        divideAt = len(sorted_vectors) // 2

        # split vectors
        vectors_left = sorted_vectors[:divideAt]
        vectors_right = sorted_vectors[divideAt:]

        # recurence
        closest_left, dist_left = dnq(vectors_left, dimension, (dvdBy+1)%(dimension-1))
        closest_right, dist_right = dnq(vectors_right, dimension, (dvdBy+1)%(dimension-1))

        # find minimum
        closest_vector, min_dist = (closest_left,dist_left) if dist_left < dist_right else (closest_right,dist_right)

        # return
        return closest_vector, min_dist

        # repeat
        # sort by x
        # divide by x
        # sort by y
        # divide by y

    else: # basis
        # find distance between 2 vectors
        dist = distance(vectors) 

        # return the two vectors and distance between them
        return vectors, dist

# by = 0, sort by x axis
# by = 1, sort by y axis
def sort(vectors, by):
    key_func = lambda vector: vector[by]
    sorted_vectors = sorted(vectors, key=key_func)
    return sorted_vectors

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
