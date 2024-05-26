# This script was used to generate figure 2a in the paper and can serve as a template for other research if required.

import matplotlib.pyplot as plt
import numpy as np

# Data - values from the CSV files in all_matchups_results
models = ["GPT-3.5-Turbo", "GPT-4-Omni"]
opponent_scores = [215, 185]
llm_scores = [185, 180]
adjusted_scores = [-30, -5]

# X-axis positions
x = np.arange(len(models))

# Bar width
width = 0.2

# Plotting
fig, ax = plt.subplots()

# Bars for opponent scores
bars1 = ax.bar(x - width, opponent_scores, width, label="Opponents Summed Score")

# Bars for total scores
bars2 = ax.bar(x, llm_scores, width, label="LLM Summed Score")

# Bars for adjusted scores
bars3 = ax.bar(x + width, adjusted_scores, width, label="LLM Adjusted Score")

ax.set_xlabel("LLMs")
ax.set_ylabel("Scores")
ax.set_title("LLM Adaptability Comparison Versus Fixed Strategies")
ax.set_xticks(x)
ax.set_xticklabels(models)

ax.set_ylim(-40, 250)
ax.set_yticks(np.arange(-40, 250, 30))

ax.legend(loc='upper right', fontsize='small')

output_path = 'data/graphs/aggregates/openai_llm_adaptability_comparison.png'
plt.savefig(output_path)

plt.show()
