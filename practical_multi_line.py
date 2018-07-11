from keras.layers import Dense
from keras.models import Sequential

size = 100

model = Sequential()
model.add(Dense(units=size, activation='relu', input_shape=(size,)))
for i in range(2, 6):
  model.add(Dense(units=int(size/i), activation='relu'))
model.add(Dense(units=5, activation='softmax'))
