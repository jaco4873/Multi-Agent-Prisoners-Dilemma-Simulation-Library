import os
from dotenv import load_dotenv

from utils.simulation import simulate_prisoners_dilemma
from helper_functions.plot_strategy_scores import plot_strategy_scores

from agent_configs.human_agent_config import human_agent
from agent_configs.llm_agent_configs import (
    selfish_gpt_4_turbo_agent, altruistic_gpt_4_turbo_agent, altruistic_gpt_35_turbo_agent, selfish_gpt_35_turbo_agent 
)
from agent_configs.fixed_strategy_agent_configs import (
    tit_for_tat_agent, suspicious_tit_for_tat_agent, forgiving_tit_for_tat_agent,
    defection_sensitive_tit_for_tat_agent, tit_for_two_tats_agent, grim_trigger_agent,
    always_cooperate_agent, adaptive_strategy_agent, soft_majority_agent,
    hard_majority_agent, random_strategy_agent, betrayal_agent
)

load_dotenv()
iterations = int(os.getenv('ITERATIONS'))

# Define matchups
matchups = [
    (adaptive_strategy_agent, betrayal_agent),
    (tit_for_tat_agent, always_cooperate_agent),
    (suspicious_tit_for_tat_agent, grim_trigger_agent)
]

# Running the simulations
for config_a, config_b in matchups:
    simulation_results = simulate_prisoners_dilemma(config_a, config_b, iterations)

datasets_directory = os.path.join('..', 'data/datasets')
graphs_directory = os.path.join('..', 'data/graphs')
plot_strategy_scores(datasets_directory, graphs_directory)