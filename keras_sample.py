from keras.layers import Dense
from keras.models import Sequential

model = Sequential([
    Dense(units=2, activation='softmax', input_shape=(3,))])
