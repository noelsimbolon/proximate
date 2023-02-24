import random

class Point:
    def __init__(self):
        self.x = random.uniform(-100,100)
        self.y = random.uniform(-100,100)
        self.z = random.uniform(-100,100)

    def printPoint(self):
        print(f'({self.x:.2f},{self.y:.2f},{self.z:.2f})')