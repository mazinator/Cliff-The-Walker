# Cliff-The-Walker
Cliff Walking Example from Book "Reinforcement Learning: Introduction" by Sutton Barto 2020, trying out SARSA and Q-learning

# Agents

4 different agents are implemented:

* RandomAgents (just does random moves)
* GodAgent (hardcoded perfect strategy)
* QLearningAgent
* SarsaAgent

The results are coherent with the original book.
QLearning leads to a rather aggressive strategy directly on the cliff's edge, while Sarsa keeps a rows distance to the cliff. 
Perfect strategy for Q-Learning if epsilon decayed to 0.

check out the parameter print_field in learn() to visualize the cliff-field in the console.