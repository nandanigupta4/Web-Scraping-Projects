import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.layers.convolutional import Conv2D
from keras.layers import Dense
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import BatchNormalization

from sklearn.metrics import classification_report

image_size = (48,48)
batch =32

train = keras.preprocessing.image_dataset_from_directory( 'Chessman-image-dataset/Chess/',
    validation_split=.2,
    subset='training',
    seed=42,
    image_size=image_size,
    batch_size=batch,
    label_mode='categorical')

validation = keras.preprocessing.image_dataset_from_directory('Chessman-image-dataset/Chess/',
    validation_split=.2,
    subset='validation',
    seed=42,
    image_size=image_size,
    batch_size=batch,
    label_mode='categorical')

''''def display_samples(dataset,n_samples,classes_name):
    plt.figure(figsize=(10,10))
    for images, labels in dataset.take(1):
        for i in range(n_samples):
            ax = plt.subplot(3,3,i+1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(classes_name[np.argmax(labels[i])])
            plt.axis("off")
            plt.show()
        
display_samples(train, 9, train.class_names)
for images, labels in train.take(1):
        for i in range(1):
            print(images[i].shape)'''

class_names = train.class_names
labels= np.array([])
for _, label in train:
    labels = np.concatenate((labels, np.argmax(label, axis=-1)))
    _, counts = np.unique(labels,return_counts = True)

print(counts)
  
input_shape = (image_size[0], image_size[1], 3)
reg = keras.regularizers.l2(0.0005)

model = keras.Sequential()
model.add(Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=image_size + (3,), kernel_regularizer=reg))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(64, (3, 3), padding="same", activation="relu", kernel_regularizer=reg))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(128, (3, 3), padding="same", activation="relu", kernel_regularizer=reg))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(len(train.class_names), activation='softmax'))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer = "adam",
metrics=["accuracy"])

epochs = 8
model.fit(train, epochs=epochs, validation_data=validation);

epochs_range = [i+1 for i in range(epochs)]
plt.plot(epochs_range,model.history.history['accuracy'],'-o',label='Train')
plt.plot(epochs_range, model.history.history['val_accuracy'], '-x',label='Validation')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')

plt.legend()
plt.show()

y_pred = np.argmax(model.predict(validation), axis=-1)
predictions = np.array([])
for x, y in validation:
    predictions = np.concatenate([predictions, np.argmax(model.predict(x), axis=-1)])
    labels = np.concatenate([labels, np.argmax(y.numpy(), axis=-1)])
conf = tf.math.confusion_matrix(labels=labels, predictions=predictions)
sns.heatmap(conf, annot=True, cmap='Blues', yticklabels=class_names, xticklabels=class_names)