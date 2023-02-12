#!/usr/bin/env python

# imports of external packages to use in our code
import sys
sys.path.append(".")

# Get our probablity config for our experiment
from Config import probs

# import our Random class from python/Random.py file
from Random import Random
random = Random()

# set up our results file for writing
result_file = open("results.txt", mode="w")

def run_experiment(prob):
    return random.Categorical(prob)

for prob in probs:
    r = []
    n_heads = 0
    for run in range(100):
        r.append(run_experiment(prob))
        n_heads += r[-1]
    result_file.write(" ".join(list(map(str, r))) + " " + str(n_heads) + "\n")
