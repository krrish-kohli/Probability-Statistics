import math
import random

N = int(input("Enter number of repetitions "))
circle = 0 # accumulator variable
not_circle = 0 # accumulator variable

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    r = math.sqrt(x**2 + y**2)

    if r < 1:
        circle += 1
    else:
        not_circle += 1

print("The value of pi is ", (circle)/(circle+not_circle)*4)
