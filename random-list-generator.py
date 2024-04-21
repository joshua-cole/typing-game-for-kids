import random
import numpy as np

roll = 0
results = []

i=0
while i < 10000:
    roll = random.randint(1,20)
    results.append(roll)
    print(roll)
    i += 1

averageRoll = np.average(results)
print(averageRoll)