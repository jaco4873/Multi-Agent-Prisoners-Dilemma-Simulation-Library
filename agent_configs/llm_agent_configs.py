from models.agent_config import AgentConfig

altruistic_gpt_4_turbo_agent = AgentConfig(
    name="Altruistic GPT-4-Turbo",
    agent_type="llm",
    llm_model="gpt-4-turbo",
    llm_personality="altruistic"
)

selfish_gpt_4_turbo_agent = AgentConfig(
    name="Selfish GPT-4-Turbo",
    agent_type="llm",
    llm_model="gpt-4-turbo",
    llm_personality="selfish"
)

altruistic_gpt_35_turbo_agent = AgentConfig(
    name="Altruistic GPT-3.5-Turbo",
    agent_type="llm",
    llm_model="gpt-3.5-turbo",
    llm_personality="altruistic"
)

selfish_gpt_35_turbo_agent = AgentConfig(
    name="Selfish GPT-3.5-Turbo",
    agent_type="llm",
    llm_model="gpt-3.5-turbo",
    llm_personality="selfish"
)