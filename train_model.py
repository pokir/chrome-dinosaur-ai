import numpy as np
import os
import tensorflow as tf
import pickle

from functions import input_file, input_dir


data_path = input_file("Training data path: ")

while True:
    use_validation_data = input("Use validation data (y/n)? ")
    if use_validation_data == "y":
        validation_data_path = input_file("Validation data path: ")

        break
    elif use_validation_data == "n":
        validation_data_path = None

while True:
    create_new_model = input("Load existing model (y/n)? ")
    if create_new_model == "y":
        model_path = input_dir("Model path: ")
        model = tf.keras.models.load_model(model_path)
        break
    elif create_new_model == "n":
        print("Creating new model")
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(65, 200, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(4)
        ])
        
        model.compile(
            optimizer="adam",
            loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"]
        )

        break

model.summary()

with open(data_path, "rb") as f:
    xs, ys = pickle.load(f)
    xs = np.array(xs)
    ys = np.array(ys)

if validation_data_path != None:
    with open(validation_data_path, "rb") as f:
        vxs, vys = pickle.load(f)
        vxs = np.array(vxs)
        vys = np.array(vys)

#print(xs.shape)
#print(ys.shape)

checkpoint_path = input("Output model path (new or existing file): ")
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=False,
    verbose=1
)

model.fit(
    xs,
    ys,
    batch_size=128,
    epochs=10,
    shuffle=True,
    callbacks=[checkpoint_callback],
    validation_data=(vxs, vys) if validation_data_path != None else None
)
