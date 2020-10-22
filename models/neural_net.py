import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#Lower batch size, way lower learning rate 500 ~ e-5!

tf.random.set_seed(12345)

df_train_x = pd.read_csv('../processed-input/prep_train_features.csv')
df_train_y = pd.read_csv('../processed-input/train_target_p.csv')

x_train = df_train_x[:20000].to_numpy()
y_train = df_train_y[:20000].to_numpy()

x_test = df_train_x[20000:].to_numpy()
y_test = df_train_y[20000:].to_numpy()

inputs = keras.Input(shape=(len(df_train_x.columns)))
x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(1024, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(1024,))(x)
x = layers.Dense(1024, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='relu')(inputs)

x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dropout(.1, input_shape=(512,))(x)
x = layers.Dense(512, activation='tanh')(inputs)

outputs = layers.Dense(len(df_train_y.columns))(x)

model = keras.Model(inputs=inputs, outputs=outputs, name="moa-first-try")
print(model.summary())

model.compile(
    loss=keras.losses.BinaryCrossentropy(label_smoothing=0),
    optimizer=keras.optimizers.Adam(learning_rate=.00006),
    metrics=["accuracy"],
)
keras.utils.plot_model(model,"model_arch_f.png", show_shapes=True, expand_nested=True)
history = model.fit(x_train, y_train, batch_size=500, epochs=1000, validation_split=0.2)
test_scores = model.evaluate(x_test, y_test, verbose=1)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])

name = 'l' + str(test_scores[0])[1:5] + '_a' + str(test_scores[1])[1:5]
if test_scores[0] <= .03:
    model.save('./nnets/great/'+name)
elif test_scores[0] <= .038:
    model.save('./nnets/good/'+name)
elif test_scores[0] <= .044:
    model.save('./nnets/decent/'+name)
elif test_scores[0] <= .05:
    model.save('./nnets/meh/'+name)