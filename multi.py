from keras.layers import Dense
from keras.models import Sequential

model = Sequential([
    Dense(units=2, activation='relu', input_shape=(4,)),
    Dense(units=3, activation='softmax')])
