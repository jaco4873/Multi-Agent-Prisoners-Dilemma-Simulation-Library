import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

def plot_strategy_scores(data_dir, graphs_dir):
    os.makedirs(graphs_dir, exist_ok=True)
    
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    for file_path in csv_files:
        
        data = pd.read_csv(file_path)
        
        plt.figure(figsize=(10, 6))
        for strategy in data['Agent Name'].unique():
            strategy_data = data[data['Agent Name'] == strategy]
            plt.plot(strategy_data['Round'], strategy_data['Score'], label=strategy)
        
        # Extract strategy names for the title
        strategy_names = data['Agent Name'].unique()
        title = f"{strategy_names[0]} vs {strategy_names[1]}"
        
        # Setting the title, labels, and legend
        plt.title(title)
        plt.xlabel('Round')
        plt.ylabel('Score')
        plt.legend(title="Strategies")
        
        # Save the plot
        plot_filename = f"{title.replace(' ', '_').replace('.', '')}.png"
        plt.savefig(os.path.join(graphs_dir, plot_filename))
        plt.close()  # Close the plot to free up memory


