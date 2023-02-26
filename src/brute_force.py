import math

def distance(p1, p2):
    global distance_count  # declare distance_count as a global variable
    distance_count += 1
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))

def closest_pair(points):
    global distance_count  # declare distance_count as a global variable
    distance_count = 0
    
    min_dist = float('inf')
    closest_pair = None
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
                
    return closest_pair, min_dist, distance_count
