import random
import coloring as cl
import process as pcs

# Splash screen

# Coloring
color = cl.Coloring()

# Read input from user
number_of_points = int(input(color.yellow("Input number of points to be generated : ")))

# Vector Dimension
VECTOR_DIMENSION = 3

# Create array of tuple (x,y,z), randomly, with each point between -100 and 100
vectors = [tuple(random.uniform(-100, 100) for _ in range(VECTOR_DIMENSION)) for _ in range(number_of_points)]

# Print points that have been generated
print(color.green("\n========POINTS========="))
print(color.yellow(vectors))

print()

closest_vectors, dist = pcs.dnq(vectors, VECTOR_DIMENSION)
print(color.magenta(f"Closest vector   : {closest_vectors}"))
print(color.blue(f"Distance         : {dist}" ))
