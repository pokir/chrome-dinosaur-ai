import cv2
import mss
import numpy as np
import os
import pprint


WIDTH = 200
HEIGHT = 65

sct = mss.mss()

# default monitor for chrome dinosaur with console open
monitor = {
    "left": 77,
    "top": 143,
    "width": 600,
    "height": 150
}


def grab_screen_raw(mon=monitor):
    try:
        raw = np.array(sct.grab(mon))
        raw = cv2.resize(raw, (WIDTH, HEIGHT))
        return raw
    except mss.ScreenShotError:
        details = sct.get_error_details()
        pprint.pprint(details)


def grab_screen(mon=monitor):
    try:
        raw = np.array(sct.grab(mon))
        raw = cv2.resize(raw, (WIDTH, HEIGHT))
        (thresh, black_and_white) = cv2.threshold(raw, 127, 255, cv2.THRESH_BINARY)
        simplified = black_and_white[:,:,0].reshape((65, 200, 1))
        return simplified
    except mss.ScreenShotError:
        details = sct.get_error_details()
        pprint.pprint(details)


def input_file(prompt):
    while True:
        answer = input(prompt)
        if os.path.isfile(answer):
            return answer
        else:
            print("File not found")


def input_dir(prompt):
    while True:
        answer = input(prompt)
        if os.path.isdir(answer):
            return answer
        else:
            print("Directory not found")
