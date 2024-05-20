import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_scores(file_path, graphs_dir):
    """
    Plots the scores of different strategies over rounds and saves the plot as a PNG file.

    Args:
        file_path (str): The path to the CSV file containing the strategy scores.
        graphs_dir (str): The directory where the plot should be saved.

    Returns:
        None
    """
    os.makedirs(graphs_dir, exist_ok=True)

    data = pd.read_csv(file_path)

    plt.figure(figsize=(10, 6))
    for strategy in data["Agent Name"].unique():
        strategy_data = data[data["Agent Name"] == strategy]
        plt.plot(strategy_data["Round"], strategy_data["Score"], label=strategy)

    strategy_names = data["Agent Name"].unique()
    title = f"{strategy_names[0]} vs {strategy_names[1]}"

    plt.title(title)
    plt.xlabel("Round")
    plt.ylabel("Score")
    plt.legend(title="Strategies")

    max_round = data["Round"].max()
    plt.xticks(range(1, max_round + 1))

    plot_filename = f"{title.replace(' ', '_').replace('.', '')}.png"
    plt.savefig(os.path.join(graphs_dir, plot_filename))
    plt.close()
