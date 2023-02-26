import random
import coloring as cl
import process as pcs
import bruteforce

# Splash screen

# Coloring
color = cl.Coloring()

# Read input from user
number_of_points = int(input(color.yellow("Input number of points to be generated : ")))

# Vector Dimension
VECTOR_DIMENSION = int(input(color.yellow("Input points dimension : ")))

# Create array of tuple (x,y,z), randomly, with each point between -100 and 100
if VECTOR_DIMENSION > 1:
    vectors = [tuple(random.uniform(-100, 100) for _ in range(VECTOR_DIMENSION)) for _ in range(number_of_points)]
else :
    vectors = [[random.uniform(-100, 100) for _ in range(VECTOR_DIMENSION)] for _ in range(number_of_points)]

# Print points that have been generated
print(color.green("\n========POINTS========="))
print(color.yellow(vectors))

print()

print(color.green("\n========DIVIDE AND CONQUER========="))
closest_vectors, dist, count = pcs.dnq(vectors, VECTOR_DIMENSION)
print(color.magenta(f"Closest vector   : {closest_vectors}"))
print(color.blue(f"Distance         : {dist}" ))
print(color.cyan(f"Count            : {count}" ))

print(color.green("\n========BRUTE FORCE========="))
closest_pairs, min_dist, distance_count = bruteforce.closest_pair(vectors)

print(color.magenta(f"Closest vector   : {closest_pairs}"))
print(color.blue(f"Distance         : {min_dist}" ))
print(color.cyan(f"Count            : {distance_count}" ))
