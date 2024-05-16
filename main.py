# ----------------------------------------------------------------------
# General Imports
# ----------------------------------------------------------------------

import os
from dotenv import load_dotenv

from utils.simulation import simulate_prisoners_dilemma
from utils.write_all_matchups_results import write_simulation_results

# ----------------------------------------------------------------------
# Agent Imports
# ----------------------------------------------------------------------

from agent_configs.human_agent_config import human_agent
from agent_configs.llm_agent_configs import (
    altruistic_gpt_4_omni_agent,
    selfish_gpt_4_omni_agent,
    default_gpt_4_omni_agent,
    altruistic_gpt_4_turbo_agent,
    selfish_gpt_4_turbo_agent,
    default_gpt_4_turbo_agent,
    altruistic_gpt_4_agent,
    selfish_gpt_4_agent,
    default_gpt_4_agent,
    altruistic_gpt_35_turbo_agent,
    selfish_gpt_35_turbo_agent,
    default_gpt_35_turbo_agent,
    altruistic_claude3_opus_agent,
    selfish_claude3_opus_agent,
    default_claude3_opus_agent,
    altruistic_claude3_sonnet_agent,
    selfish_claude3_sonnet_agent,
    default_claude3_sonnet_agent,
    altruistic_claude3_haiku_agent,
    selfish_claude3_haiku_agent,
    default_claude3_haiku_agent,
    altruistic_command_agent,
    selfish_command_agent,
    default_command_agent,
    altruistic_command_light_agent,
    selfish_command_light_agent,
    default_command_light_agent,
    altruistic_command_r_agent,
    selfish_command_r_agent,
    default_command_r_agent,
    altruistic_command_r_plus_agent,
    selfish_command_r_plus_agent,
    default_command_r_plus_agent,
    altruistic_mistral_7b_agent,
    selfish_mistral_7b_agent,
    default_mistral_7b_agent,
    altruistic_mixtral_8x7b_agent,
    selfish_mixtral_8x7b_agent,
    default_mixtral_8x7b_agent,
    altruistic_mixtral_8x22b_agent,
    selfish_mixtral_8x22b_agent,
    default_mixtral_8x22b_agent,
    altruistic_mistral_small_agent,
    selfish_mistral_small_agent,
    default_mistral_small_agent,
    altruistic_mistral_medium_agent,
    selfish_mistral_medium_agent,
    default_mistral_medium_agent,
    altruistic_mistral_large_agent,
    selfish_mistral_large_agent,
    default_mistral_large_agent,
    altruistic_gemini_1_pro_agent,
    selfish_gemini_1_pro_agent,
    default_gemini_1_pro_agent,
)


from agent_configs.fixed_strategy_agent_configs import (
    tit_for_tat_agent,
    suspicious_tit_for_tat_agent,
    forgiving_tit_for_tat_agent,
    defection_sensitive_tit_for_tat_agent,
    tit_for_two_tats_agent,
    grim_trigger_agent,
    always_cooperate_agent,
    adaptive_strategy_agent,
    soft_majority_agent,
    hard_majority_agent,
    random_strategy_agent,
    betrayal_agent,
)

from prompts.choice_prompts.choice_prompt_without_reasoning import (
    choice_prompt_without_reasoning,
)
from prompts.choice_prompts.choice_prompt_with_reasoning import (
    choice_prompt_with_reasoning,
)

# ----------------------------------------------------------------------
# Run Simulations
# ----------------------------------------------------------------------


load_dotenv()
iterations = int(os.getenv("ITERATIONS"))

# Define matchups in a list of tuples
matchups = [
    (altruistic_gpt_35_turbo_agent, always_cooperate_agent),
    (altruistic_gpt_35_turbo_agent, random_strategy_agent),
]

# Running the simulations
results = []
for config_a, config_b in matchups:
    simulation_results = simulate_prisoners_dilemma(
        config_a,
        config_b,
        iterations,
        choice_prompt=choice_prompt_with_reasoning,  # change choice prompt if required
    )
    results.append(simulation_results)

write_simulation_results(results)
