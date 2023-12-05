#Author: Alican Akca (12/5/2023)

# Import necessary libraries
import gym
import numpy as np
import imageio
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import Callback, TensorBoard
from kerastuner.tuners import RandomSearch
from keras.layers import Dropout, BatchNormalization
from keras.activations import relu, elu, sigmoid

# Define the RL environment
env = gym.make('CartPole-v1')

def build_model(hp):
    model = Sequential()
    # Increase the number of layers
    for i in range(hp.Int('num_layers', 2, 10)):
        # Increase the number of units in each layer
        model.add(Dense(units=hp.Int('units_' + str(i), min_value=32, max_value=1024, step=32), input_dim=4))
        # Add Batch Normalization
        if hp.Choice('batch_normalization_' + str(i), values=[0, 1]):
            model.add(BatchNormalization())
        # Add Activation
        model.add(Activation(hp.Choice('activation_' + str(i), values=['relu', 'elu', 'sigmoid'])))
        # Add Dropout
        if hp.Choice('dropout_' + str(i), values=[0, 1]):
            model.add(Dropout(rate=hp.Float('dropout_rate_' + str(i), min_value=0.0, max_value=0.5, step=0.1)))
    model.add(Dense(units=2))
    model.add(Activation('linear'))
    model.compile(loss='mse', optimizer=Adam(hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])))
    return model

# Initialize the tuner
tuner = RandomSearch(
    build_model,
    objective='val_loss',
    max_trials=1,
    executions_per_trial=1,
    directory='test_directory',
    project_name='hyperparam_opt'
)

# Perform hyperparameter search
tuner.search_space_summary()

# Define the TensorBoard callback
tb_callback = TensorBoard(log_dir='./logs', histogram_freq=1)

# Define a custom callback for creating GIFs
class GifCallback(Callback):
    def on_train_begin(self, logs={}):
        self.images = []

    def on_epoch_end(self, epoch, logs={}):
        # Reset the environment
        state = env.reset()
        done = False
        # Step through the environment
        while not done:
            # Render the environment and add the image to the list
            self.images.append(env.render(mode='rgb_array'))
            # Take a random action
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
        # Save images as a GIF
        imageio.mimsave(f'train_{epoch+1}.gif', self.images, fps=30)
        # Clear the images list for the next epoch
        self.images.clear()

gif_callback = GifCallback()

tuner.search(x=np.array([env.reset()]*100), y=np.array([[0,0]]*100), epochs=3000, validation_data=(np.array([env.reset()]*20), np.array([[0,0]]*20)), callbacks=[tb_callback, gif_callback])
