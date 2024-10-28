import matplotlib.pyplot as plt

def plot_result(metadata, skip=0):
    plt.figure(figsize=(12, 8))

    # Extract 'avg_reward' and 'episode_round' from each entry in metadata['data']
    rewards = [entry['total_reward'] for entry in metadata['data'] if entry['episode_round'] >= skip]
    episode_rounds = [entry['episode_round'] for entry in metadata['data'] if entry['episode_round'] >= skip]

    # Plot a line connecting all avg_reward values
    plt.plot(episode_rounds, rewards, marker='o', linestyle='-', color='b')

    # Title and labels using metadata
    plt.title(f"Average Reward over Time ({metadata['agent']} - {metadata['episodes']} episodes)", fontsize=16)
    plt.xlabel('Episode Round', fontsize=14)
    plt.ylabel('Average Reward', fontsize=14)

    # Display the plot
    plt.grid(True)
    if metadata['agent'] == 'QLearning':
        plt.savefig(f'figures/{metadata['agent']}_{metadata["episodes"]}episodes_.png')
    else:
        plt.savefig(f'figures/{metadata['agent']}_{metadata["episodes"]}_episodes.png')
