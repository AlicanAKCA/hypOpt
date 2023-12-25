# hypOpt
Provides to optimize the hyperparameters using Reinforcement Learning. Term Project for the Optimization course  at Izmir University of Economics.

# Methodology
## Agent
The agent makes decisions by choosing actions that are expected to maximize the cumulative reward over time. The agent is a neural network model that takes the state of the environment as input and outputs the action to be taken.

## Optimization Problem
The objective function is to minimize the validation loss (val_loss) which is the Mean Squared Error (MSE). Given a set of n samples, where for each sample i, the predicted value is y^ i and the actual value is yi , the MSE is calculated as:

<a name="logo"/>
<div align="center">
<a href="https://github.com/AlicanAKCA/hypOpt" target="_blank">
<img src="https://github.com/AlicanAKCA/hypOpt/assets/27694294/ee26d1c6-ee81-42ab-802c-1015555a1e32" alt="" width="220" height="50"></img>
</a>
</div>

## Rewards and Penalties 
In the context of reinforcement learning, Q-values that must be maximized represent the expected future reward for taking a certain action in a certain state. where:

<a name="logo"/>
<div align="center">
<a href="https://github.com/AlicanAKCA/hypOpt" target="_blank">
<img src="https://github.com/AlicanAKCA/hypOpt/assets/27694294/a3643bec-6cf8-48a2-ab23-15879fe0e1d9" alt="" width="240" height="50"></img>
</a>
</div>




<p>● s is the current state <br>

<p>● a is the action taken,<br>

<p>● r is the immediate reward received after taking action a in state s,<br>

<p>● s′ is the new state after taking action a,<br>

<p>● a′ is the action taken in state s′,<br>

<p>● γ is the discount factor which determines the present value of future rewards.<br>

# Algorithm
## Random Search
Let f: ℝ
n
 → ℝ be the fitness or cost function which must be minimized. Let x ∈ ℝ
n
 designate a position or
candidate solution in the search-space. The basic RandomSearch algorithm can then be described as:
1. Initialize x with a random position in the search-space.
2. Until a termination criterion is met (e.g. number of iterations performed, or adequate fitness reached),
repeat the following:
    1. Sample a new position y from the hypersphere of a given radius surrounding the current
    position x (see e.g. Marsaglia's technique for sampling a hypersphere.)
    2. If f(y) < f(x) then move to the new position by setting x = y


You can access the Tutorial and all inferences below.

<a name="logo"/>
<div align="center">
<a href="https://colab.research.google.com/drive/11AM-_-yduAoIiw_wqqQ9jMgnTw4a2sJY?usp=sharing" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="" width="170" height="30"></img>
</a>
</div>

<a name="logo"/>
<div align="center">
<a href="https://drive.google.com/file/d/1HhJZrQsWBLVTelCYu_RCwY07xX1MTTRT/view?usp=sharing" target="_blank">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Drive_icon_%282020%29.svg/1147px-Google_Drive_icon_%282020%29.svg.png" alt="" width="30" height="30"></img>
</a>
</div>


# References

[1] Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problems ANDREW G.
BARTO, Member, IEEE, Richard S. Sutton, and Charles w. Anderson (0018-9472/83/0900-083401.00 01983
IEEE)
