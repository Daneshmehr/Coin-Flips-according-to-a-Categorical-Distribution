#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random
random = Random()

def run_experiment(prob):
    return random.Categorical(prob)

results = []
n_heads = []
probs = [0.5, 0.75]
for prob in probs:
    r = []
    n = 0
    for run in range(100):
        r.append(run_experiment(prob))
        n += r[-1]
    results.append(r)
    n_heads.append(n)

colors = ["red", "green"]
figure, axis = plt.subplots(1,2)
for i in range(len(results)):
    print("p = ", end='')
    print(probs[i], end=': ')
    print(results[i], end="\n\n")
    axis[i].bar(["heads", "tails"], [n_heads[i], (len(results[i]) - n_heads[i])], color=colors[i])
    axis[i].set_title(str(probs[i]))
    
plt.ylabel('Probability')

plt.show()