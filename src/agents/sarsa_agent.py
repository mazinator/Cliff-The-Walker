import time

import numpy as np


class SarsaAgent:
    def __init__(self, cliff_board, alpha=0.1, gamma=0.9, epsilon=0.1, epsilon_decay=0.995):
        self.cliff_board = cliff_board
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.q_table = np.zeros(
            (self.cliff_board.rows, self.cliff_board.cols, len(self.actions)))  # state-action values
        self.last_results = None
        self.epsilon_decay = epsilon_decay

    def choose_action(self, state):
        """
        Chooses an action using an ε-greedy policy.
        """
        if np.random.random() < self.epsilon:
            # Exploration: choose a random action
            return np.random.choice(self.actions)
        else:
            # Exploitation: choose the action with the highest Q-value for the current state
            state_row, state_col = state
            action_idx = np.argmax(self.q_table[state_row, state_col, :])
            return self.actions[action_idx]

    def update_q_value(self, state, action, reward, next_state, next_action):
        """
        Updates the Q-value for the given state and action using the SARSA formula.
        """
        state_row, state_col = state
        next_state_row, next_state_col = next_state
        action_idx = self.actions.index(action)
        next_action_idx = self.actions.index(next_action)

        # Current Q-value
        current_q_value = self.q_table[state_row, state_col, action_idx]

        # SARSA formula using Q(s', a') for next action in next state
        next_q_value = self.q_table[next_state_row, next_state_col, next_action_idx]
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * next_q_value - current_q_value)

        # Update Q-table
        self.q_table[state_row, state_col, action_idx] = new_q_value

    def learn(self, episodes=1000, print_field=float('inf')):
        """
        Learn the Q-values over a series of episodes using Sarsa.
        """
        results = {'data': [],
                   'agent': self.__class__.__name__,
                   'episodes': episodes}

        for i in range(1, episodes + 1):

            episode_data = {
                'episode_round': i,
                'steps': [],
                'total_reward': 0,
                'step_count': 0
            }

            self.cliff_board.reset()

            steps = 0
            total_reward = 0.0

            state = self.cliff_board.get_state()
            action = self.choose_action(state)

            # As long as episode is not finished
            while not self.cliff_board.is_terminal():
                steps += 1

                reward = self.cliff_board.make_action(action)
                next_state = self.cliff_board.get_state()
                next_action = self.choose_action(next_state)

                self.update_q_value(state, action, reward, next_state, next_action)

                state, action = next_state, next_action
                total_reward += reward

                # Store episode data for analysis
                step_data = {
                    'step_number': steps,
                    'action_taken': action,
                    'reward': reward,
                }
                episode_data['steps'].append(step_data)

                if i > print_field:
                    time.sleep(0.03)
                    self.cliff_board.print_board(text=f"{self.__class__.__name__}, episode {i}")

            episode_data['total_reward'] = total_reward
            episode_data['step_count'] = steps

            # Store the entire episode data
            results['data'].append(episode_data)

            self.epsilon *= self.epsilon_decay

            if self.epsilon < 1e-5 or i > 600:
                self.epsilon = 0

        self.last_results = results
        return results
