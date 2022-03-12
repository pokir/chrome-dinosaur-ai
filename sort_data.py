import numpy as np
import pickle
import os
from random import random, shuffle

from functions import input_file


data_path = input_file("Data path: ")

if os.path.getsize(data_path) > 0:
    with open(data_path, "rb") as f:
        xs, ys = pickle.load(f)

new_xs = []
new_ys = []

# reduce amount of nothing
for i in range(len(ys)):
    if ys[i][0] == 1 and random() < 0.95:
        continue

    new_xs.append(xs[i])
    new_ys.append(ys[i])

# shuffles automatically in model.fit
#c = list(zip(new_xs, new_ys))
#shuffle(c)
#new_xs, new_ys = zip(*c)

# output
output_data_path = input("Output data path: ")
with open(output_data_path, "wb") as f:
    pickle.dump((new_xs, new_ys), f)
