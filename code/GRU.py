import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

# Create sample data
X_train = tf.random.normal((100, 10, 5))
y_train = tf.random.uniform((100,), maxval=2, dtype=tf.int32)

# Create model
model = Sequential()

# Add GRU layer
model.add(GRU(64, input_shape=(10, 5)))

# Add hidden layer
model.add(Dense(32, activation='relu'))

# Add output layer
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=5, batch_size=16)

# Display model summary
model.summary()