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

vectors = [(50.572799210020094, 83.15402995504587, 43.57900364087348), 
           (-28.885983623645558, -1.5488497740578708, 10.598584194109065), 
           (-89.61165627908294, 14.165609770503067, -79.31865904879712), 
           (-12.535935067584262, 46.42547937023019, 99.9688164471481), 
           (41.88775573477139, 56.67617235079277, 20.51898520442208), 
           (0.5414408505394448, -82.30758932481517, -41.19101128982159), 
           (-73.0334115919971, 36.76972671749243, 51.30924915733209), 
           (80.27710476887856, 34.412885675091786, 95.87915684444215), 
           (14.505662446880606, 28.093157016376438, -24.31732344755673), 
           (32.41555972051634, 44.64304393191881, 98.14785777564083)]

# Print points that have been generated
print(color.green("\n========POINTS========="))
print(color.yellow(vectors))

print()

closest_vectors, dist, count = pcs.dnq(vectors, VECTOR_DIMENSION)
print(color.magenta(f"Closest vector   : {closest_vectors}"))
print(color.blue(f"Distance         : {dist}" ))
print(color.cyan(f"Count            : {count}" ))
