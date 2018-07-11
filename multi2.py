from keras.layers import Dense
from keras.models import Sequential

model = Sequential()
model.add(Dense(units=2, activation='relu', input_shape=(4,)))
model.add(Dense(units=3, activation='softmax'))
