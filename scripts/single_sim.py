import os
from dotenv import load_dotenv

from utils.simulation import simulate_prisoners_dilemma

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

from prompts.choice_prompts.choice_prompt_without_reasoning import choice_prompt_without_reasoning
from prompts.choice_prompts.choice_prompt_with_reasoning import choice_prompt_with_reasoning


load_dotenv(verbose=True)
iterations = int(os.getenv('ITERATIONS'))

final_results = simulate_prisoners_dilemma(config_a = hard_majority_agent, config_b = soft_majority_agent, iterations=iterations, choice_prompt=choice_prompt_with_reasoning)

print(final_results)