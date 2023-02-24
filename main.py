import point as pt
import coloring as cl

# Splash screen

# Coloring
color = cl.Coloring()

# Read input from user
number_of_points = int(input(color.yellow("Input number of points to be generated : ")))

# Create array of Point
points = [pt.Point() for _ in range (number_of_points)]

# Print points that have been generated
print(color.green("\n========POINTS========="))
for poins in points:
    poins.printPoint()


