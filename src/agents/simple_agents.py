import time

import numpy as np
from src.environment.board import CliffBoard


# very stupid baseline - always random moves, no learning
class RandomAgent():
    def __init__(self, cliff_board: CliffBoard):
        self.cliff_board = cliff_board
        self.last_results = None

    def choose_action(self):
        action = np.random.randint(1, 5)
        if action == 1:
            return 'UP'
        if action == 2:
            return 'DOWN'
        if action == 3:
            return 'LEFT'
        if action == 4:
            return 'RIGHT'
        else:
            raise ValueError('Invalid action')

    def learn(self, episodes=1000):
        """
        learning is an overstatement, as it is just random stuff
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

            # as long as episode is not finished
            while not self.cliff_board.is_terminal():
                steps += 1

                # pick next action
                action = self.choose_action()

                # get next state,
                reward = self.cliff_board.make_action(action)

                total_reward += reward

                # store board states for analysis
                step_data = {
                    'step_number': steps,
                    'action_taken': action,
                    #'board_state': np.copy(self.cliff_board.board),
                    'reward': reward
                }
                episode_data['steps'].append(step_data)

            episode_data['total_reward'] = total_reward
            episode_data['step_count'] = steps

            # Store the entire episode data
            results['data'].append(episode_data)

        self.last_results = results
        return results


# knows the perfect moves
class GodAgent():
    def __init__(self, cliff_board):
        self.cliff_board = cliff_board

    def learn(self, episodes=1000):

        results = {'data': [],
                   'agent': self.__class__.__name__,
                   'episodes': episodes}

        for i in range(episodes):

            episode_data = {
                'episode_round': i,
                'steps': [],
                'total_reward': 0,
                'step_count': 0
            }

            self.cliff_board.reset()

            total_reward = 0.0

            total_reward += self.cliff_board.make_action('UP')

            for j in range(1, 13):
                total_reward += self.cliff_board.make_action('RIGHT')
                #self.delayed_board_printing()

            total_reward += self.cliff_board.make_action('DOWN')
            #self.delayed_board_printing()

            #print(f'Episode {i} done with reward: {total_reward}')

    def delayed_board_printing(self, t=0.1):
        time.sleep(t)
        self.cliff_board.print_board()
