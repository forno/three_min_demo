model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# dummy data creation (noisy section)
import numpy as np
data = np.random.random((1000, 3))
labels = np.random.randint(2, size=(1000, 1))
labels = keras.utils.to_categorical(labels, num_classes=2) # encode to one-hot vector

# model training
model.fit(data, labels, epochs=10, batch_size=32)
