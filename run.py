from src.simple_agents import *
from src.results import plot_result
def main():
    boardRandom = CliffBoard()
    boardGod = CliffBoard()

    godAgent = GodAgent(boardGod)
    data = godAgent.learn()

    # 1 - check figures random baseline
    randomAgent = RandomAgent(boardRandom)
    data = randomAgent.learn()
    plot_result(data)
    #print(data)









if __name__ == '__main__':
    main()
