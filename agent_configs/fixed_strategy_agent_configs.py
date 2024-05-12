from models.agent_config import AgentConfig
from utils.fixed_strategies import (
    tit_for_tat,
    suspicious_tit_for_tat,
    forgiving_tit_for_tat,
    defection_sensitive_tit_for_tat,
    tit_for_two_tats,
    grim_trigger,
    always_cooperate,
    adaptive_strategy,
    soft_majority,
    hard_majority,
    random_strategy,
    betrayal,
)

# Configurations

tit_for_tat_agent = AgentConfig(
    name="Tit For Tat", agent_type="fixed", fixed_strategy=tit_for_tat
)

suspicious_tit_for_tat_agent = AgentConfig(
    name="Suspicious Tit For Tat",
    agent_type="fixed",
    fixed_strategy=suspicious_tit_for_tat,
)

forgiving_tit_for_tat_agent = AgentConfig(
    name="Forgiving Tit For Tat",
    agent_type="fixed",
    fixed_strategy=forgiving_tit_for_tat,
)

defection_sensitive_tit_for_tat_agent = AgentConfig(
    name="Defection Sensitive Tit For Tat",
    agent_type="fixed",
    fixed_strategy=defection_sensitive_tit_for_tat,
)

tit_for_two_tats_agent = AgentConfig(
    name="Tit For Two Tats", agent_type="fixed", fixed_strategy=tit_for_two_tats
)

grim_trigger_agent = AgentConfig(
    name="Grim Trigger", agent_type="fixed", fixed_strategy=grim_trigger
)

always_cooperate_agent = AgentConfig(
    name="Always Cooperate", agent_type="fixed", fixed_strategy=always_cooperate
)

adaptive_strategy_agent = AgentConfig(
    name="Adaptive Strategy", agent_type="fixed", fixed_strategy=adaptive_strategy
)

soft_majority_agent = AgentConfig(
    name="Soft Majority", agent_type="fixed", fixed_strategy=soft_majority
)

hard_majority_agent = AgentConfig(
    name="Hard Majority", agent_type="fixed", fixed_strategy=hard_majority
)

random_strategy_agent = AgentConfig(
    name="Random Strategy", agent_type="fixed", fixed_strategy=random_strategy
)

betrayal_agent = AgentConfig(
    name="Betrayal", agent_type="fixed", fixed_strategy=betrayal
)
