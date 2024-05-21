import pandas as pd
import matplotlib.pyplot as plt
import os
import uuid
from utils.sanitize_file_name import sanitize_filename

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

    # Check if there are exactly two unique agent names
    unique_agent_names = data["Agent Name"].unique()
    if len(unique_agent_names) == 2:
        # There are exactly two unique names, no need to add identifier
        data["Unique Agent Name"] = data["Agent Name"]
    else:
        # Names are not unique, add an identifier
        data['Agent Identifier'] = data.groupby('Round').cumcount() + 1
        data['Unique Agent Name'] = data['Agent Name'] + ' ' + data['Agent Identifier'].astype(str)

    plt.figure(figsize=(10, 6))

    # Plot the scores for each agent
    for strategy in data["Unique Agent Name"].unique():
        strategy_data = data[data["Unique Agent Name"] == strategy]
        plt.plot(strategy_data["Round"], strategy_data["Score"], label=strategy)

    # Create a title for the plot using the first two unique agent names
    strategy_names = data["Unique Agent Name"].unique()
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
