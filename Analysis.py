#!/usr/bin/env python

# imports of external packages to use in our code
import sys
sys.path.append(".")

# Get our probablity config for our experiment
from Config import probs

# imports of external packages to use in our code
import matplotlib.pyplot as plt

result_file = open("results.txt", mode="r")

results = []
n_heads = []

for line in result_file.readlines():
    line = line.rstrip().split(" ")
    r, heads = line[:-1], line[-1]
    results.append([float(result) for result in r])
    n_heads.append(float(heads))

colors = ["red", "green"]
figure, axis = plt.subplots(1,2)
for i in range(len(results)):
    print("p = ", end='')
    print(probs[i], end=': ')
    print(results[i], end="\n\n")
    axis[i].bar(["heads", "tails"], [n_heads[i], (len(results[i]) - n_heads[i])], color=colors[i])
    axis[i].set_title(str(probs[i]))
    
plt.ylabel('number of coin flips')

plt.show()
