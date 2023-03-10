import os
import caer

import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler

IMG_SIZE = (80, 80)
channels = 1
char_path = r"../Resources/simpsons_dataset"

# Creating a character dictionary, sorting it in descending order
char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

# Sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
print(char_dict)

count = 0
characters = []
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break
print(characters)

# Create the training data
train = caer.preprocess_from_dir(
    char_path, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True
)

print(len(train))

plt.figure(figsize=(30, 30))
plt.imshow(train[0][0], cmap="gray")
plt.show()

featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)

# Normalize the feature set featureSet==>(0,1)
featureSet = caer.normalize(featureSet)
labels = to_categorical(labels, len(characters))

x_train, x_val, y_train, y_val = caer.train_val_split(featureSet, labels, val_ratio=0.2)

del train
del featureSet
del labels
gc.collect()

BATCH_SIZE = 32
EPOCHS = 10

# Image data generator
datagen = canaro.generators.imageDataGenerator()
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)


# Creating the model
model = canaro.models.createSimpsonsModel(
    IMG_SIZE=IMG_SIZE,
    channels=channels,
    output_dim=len(characters),
    loss="binary_crossentropy",
    decay=1e-6,
    learning_rate=0.001,
    momentum=0.9,
    nesterov=True,
)

model.summary()

callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

training = model.fit(
    train_gen,
    steps_per_epoch=len(x_train) // BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=(x_val, y_val),
    validation_steps=len(y_val) // BATCH_SIZE,
    callbacks=callbacks_list,
)

test_path = r"../Resources/kaggle_simpson_testset/kaggle_simpson_testset/apu_nahasapeemapetilon_20.jpg"
img = cv.imread(test_path)


def prepare(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, IMG_SIZE)
    img = caer.reshape(img, IMG_SIZE, 1)
    return img


predictions = model.predict(prepare(img))
print(predictions)

print("What model said:")
print(characters[np.argmax(predictions[0])])
