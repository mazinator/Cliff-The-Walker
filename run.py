from src.agents.simple_agents import *
from src.utils.results_printer import plot_result
from src.agents.sarsa_agent import SarsaAgent
from src.agents.q_learning_agent import QLearningAgent


def main():
    board = CliffBoard()

    agents = [RandomAgent, GodAgent, QLearningAgent, SarsaAgent]

    for agent in agents:
        print(f"Running {agent.__name__} ...")
        agent_instance = agent(board)
        data = agent_instance.learn(episodes=500)

        if data:  # not implemented for the simple agents
            plot_result(data)

            # Calc avg rewards
            rewards = [entry['total_reward'] for entry in data['data']]
            print(f'Average reward for {agent.__name__} over {len(rewards)} episodes: {sum(rewards) / len(rewards)}')


if __name__ == '__main__':
    main()
