from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils

y = np_utils.to_categorical(y_new)

model = Sequential()
model.add(Dense(32,activation = 'relu', input_dim = 25))
#model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation = 'softmax'))
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(X_train, y_train, validation_data = (X_test,y_test),batch_size = 32, epochs = 5, verbose = 1)
