import cv2
import keyboard
import numpy as np
import os
import pickle
#import pprint
import time

from functions import grab_screen


data_path = input("Data path: ")

if os.path.isfile(data_path) and os.path.getsize(data_path) > 0:
    with open(data_path, "rb") as f:
        xs, ys = pickle.load(f)
else:
    xs = [] # pixels
    ys = [] # jump (0, 1, 0, 0), down (0, 0, 1, 0), enter (0, 0, 0, 1), or nothing (1, 0, 0, 0)

for i in range(5):
    print(5 - i)
    time.sleep(1)

while True:
    x = grab_screen()
    cv2.imshow("Creating data", x)
    
    y = np.array([1, 0, 0, 0])
    try:
        if keyboard.is_pressed(" ") or keyboard.is_pressed("up"):
            y = np.array([0, 1, 0, 0])
        elif keyboard.is_pressed("down"):
            y = np.array([0, 0, 1, 0])
        elif keyboard.is_pressed("enter"):
            y = np.array([0, 0, 0, 1])

        elif keyboard.is_pressed("q"):
            break
    except:
        pass

    xs.append(x)
    ys.append(y)

    cv2.waitKey(1) # it won't work without this

# clean up
cv2.destroyAllWindows()

#print(xs[0].shape)

while True:
    save = input("Save (y/n)? ")

    if save == "y":
        with open(data_path, "wb") as f:
            pickle.dump((xs, ys), f)
            break
    elif save == "n":
        break
