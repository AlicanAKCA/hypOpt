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
   
## To-Do List
- [ ] Colab Tutorial
- [ ] Adding reqiurements.txt (has been specifying the versions of the libraries.
- [x] Add Main Script
- [ ] Add Article and Presentations
- [ ] Inferences and Evalutations
- [ ] Videos
