import random
import numpy as np

roll = 0
results = []

i=0
while i < 1000000:
    results.append(random.randint(1,20))
    i += 1
averageRoll = np.average(results)
print(averageRoll)