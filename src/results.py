import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

"""def plot_hist(metadata):
    rewards = [entry['avg_reward'] for entry in metadata['data']]
    episode_rounds = [entry['episode_round'] for entry in metadata['data']]

    plt.figure(figsize=(12,8))
    plt.title(f'Average reward per episode of {metadata['agent']} with {metadata['episodes']} episodes')
    plt.plot(episode_rounds, rewards, marker='o', linestyle='-', color='b')
"""

def plot_result(metadata):
    plt.figure(figsize=(12, 8))

    # Extract 'avg_reward' and 'episode_round' from each entry in metadata['data']
    rewards = [entry['total_reward'] for entry in metadata['data']]
    episode_rounds = [entry['episode_round'] for entry in metadata['data']]

    # Plot a line connecting all avg_reward values
    plt.plot(episode_rounds, rewards, marker='o', linestyle='-', color='b')

    # Title and labels using metadata
    plt.title(f"Average Reward over Time ({metadata['agent']} - {metadata['episodes']} episodes)", fontsize=16)
    plt.xlabel('Episode Round', fontsize=14)
    plt.ylabel('Average Reward', fontsize=14)

    # Display the plot
    plt.grid(True)
    plt.savefig(f'figures/{metadata['agent']}_{metadata["episodes"]}_episodes.png')
