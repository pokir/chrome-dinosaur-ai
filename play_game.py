#import cv2
import keyboard
import numpy as np
import pickle
import tensorflow as tf
import time

from functions import grab_screen, input_dir


def do_action(num):
    if num == 0:
        pass
    elif num == 1:
        keyboard.press(" ")
    elif num == 2:
        keyboard.press("down")
    elif num == 3:
        keyboard.press("enter")


def end_action(num):
    if num == 0:
        pass
    elif num == 1:
        keyboard.release(" ")
    elif num == 2:
        keyboard.release("down")
    elif num == 3:
        keyboard.release("enter")


model_path = input_dir("Model path: ")

probability_model = tf.keras.Sequential([
    tf.keras.models.load_model(model_path),
    tf.keras.layers.Softmax()
])
#probability_model = tf.keras.models.load_model(model_path)

probability_model.summary()

#actions = ["nothing", "jump", "down", "enter"]

for i in range(5):
    print(5 - i)
    time.sleep(1)

last_action = None

while True:
    x = grab_screen()

    y = probability_model.predict(np.array([x]))
    action = y.argmax()

    if action != last_action:
        end_action(last_action)
        do_action(action)

    last_action = action
    
    #cv2.imshow("OpenCV/Numpy normal", screen)
