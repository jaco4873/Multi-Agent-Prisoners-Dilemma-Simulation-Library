from models.agent_config import AgentConfig

# ----------------------------------------------------------------------
# OpenAI
# ----------------------------------------------------------------------

# GPT-4 Turbo
altruistic_gpt_4_turbo_agent = AgentConfig(
    name="Altruistic GPT-4-Turbo",
    agent_type="llm",
    llm_model="gpt-4-turbo",
    llm_personality="altruistic",
)

selfish_gpt_4_turbo_agent = AgentConfig(
    name="Selfish GPT-4-Turbo",
    agent_type="llm",
    llm_model="gpt-4-turbo",
    llm_personality="selfish",
)

default_gpt_4_turbo_agent = AgentConfig(
    name="Default GPT-4-Turbo",
    agent_type="llm",
    llm_model="gpt-4-turbo",
    llm_personality="default",
)

# GPT-3.5 Turbo
altruistic_gpt_35_turbo_agent = AgentConfig(
    name="Altruistic GPT-3.5-Turbo",
    agent_type="llm",
    llm_model="gpt-3.5-turbo",
    llm_personality="altruistic",
)

selfish_gpt_35_turbo_agent = AgentConfig(
    name="Selfish GPT-3.5-Turbo",
    agent_type="llm",
    llm_model="gpt-3.5-turbo",
    llm_personality="selfish",
)

default_gpt_35_turbo_agent = AgentConfig(
    name="Default GPT-3.5-Turbo",
    agent_type="llm",
    llm_model="gpt-3.5-turbo",
    llm_personality="default",
)

# ----------------------------------------------------------------------
# Anthropic
# ----------------------------------------------------------------------

# Claude 3 Opus
altruistic_claude3_opus_agent = AgentConfig(
    name="Altruistic Claude 3 Opus",
    agent_type="llm",
    llm_model="claude-3-opus-20240229",
    llm_personality="altruistic",
)

selfish_claude3_opus_agent = AgentConfig(
    name="Selfish Claude 3 Opus",
    agent_type="llm",
    llm_model="claude-3-opus-20240229",
    llm_personality="selfish",
)

default_claude3_opus_agent = AgentConfig(
    name="Default Claude 3 Opus",
    agent_type="llm",
    llm_model="claude-3-opus-20240229",
    llm_personality="default",
)

# Claude 3 Sonnet
altruistic_claude3_sonnet_agent = AgentConfig(
    name="Altruistic Claude 3 Sonnet",
    agent_type="llm",
    llm_model="claude-3-sonnet-20240229",
    llm_personality="altruistic",
)

selfish_claude3_sonnet_agent = AgentConfig(
    name="Selfish Claude 3 Sonnet",
    agent_type="llm",
    llm_model="claude-3-sonnet-20240229",
    llm_personality="selfish",
)

default_claude3_sonnet_agent = AgentConfig(
    name="Default Claude 3 Sonnet",
    agent_type="llm",
    llm_model="claude-3-sonnet-20240229",
    llm_personality="default",
)

# Claude 3 Haiku
altruistic_claude3_haiku_agent = AgentConfig(
    name="Altruistic Claude 3 Haiku",
    agent_type="llm",
    llm_model="claude-3-haiku-20240307",
    llm_personality="altruistic",
)

selfish_claude3_haiku_agent = AgentConfig(
    name="Selfish Claude 3 Haiku",
    agent_type="llm",
    llm_model="claude-3-haiku-20240307",
    llm_personality="selfish",
)

default_claude3_haiku_agent = AgentConfig(
    name="Default Claude 3 Haiku",
    agent_type="llm",
    llm_model="claude-3-haiku-20240307",
    llm_personality="default",
)

# ----------------------------------------------------------------------
# COHERE
# ----------------------------------------------------------------------

# Command
altruistic_command_agent = AgentConfig(
    name="Altruistic Command",
    agent_type="llm",
    llm_model="command",
    llm_personality="altruistic",
)

selfish_command_agent = AgentConfig(
    name="Selfish Command",
    agent_type="llm",
    llm_model="command",
    llm_personality="selfish",
)

default_command_agent = AgentConfig(
    name="Default Command",
    agent_type="llm",
    llm_model="command",
    llm_personality="default",
)

# Command-Light
altruistic_command_light_agent = AgentConfig(
    name="Altruistic Command-Light",
    agent_type="llm",
    llm_model="command-light",
    llm_personality="altruistic",
)

selfish_command_light_agent = AgentConfig(
    name="Selfish Command-Light",
    agent_type="llm",
    llm_model="command-light",
    llm_personality="selfish",
)

default_command_light_agent = AgentConfig(
    name="Default Command-Light",
    agent_type="llm",
    llm_model="command-light",
    llm_personality="default",
)

# Command-R
altruistic_command_r_agent = AgentConfig(
    name="Altruistic Command-R",
    agent_type="llm",
    llm_model="command-r",
    llm_personality="altruistic",
)

selfish_command_r_agent = AgentConfig(
    name="Selfish Command-R",
    agent_type="llm",
    llm_model="command-r",
    llm_personality="selfish",
)

default_command_r_agent = AgentConfig(
    name="Default Command-R",
    agent_type="llm",
    llm_model="command-r",
    llm_personality="default",
)

# Command-R-Plus
altruistic_command_r_plus_agent = AgentConfig(
    name="Altruistic Command-R-Plus",
    agent_type="llm",
    llm_model="command-r-plus",
    llm_personality="altruistic",
)

selfish_command_r_plus_agent = AgentConfig(
    name="Selfish Command-R-Plus",
    agent_type="llm",
    llm_model="command-r-plus",
    llm_personality="selfish",
)

default_command_r_plus_agent = AgentConfig(
    name="Default Command-R-Plus",
    agent_type="llm",
    llm_model="command-r-plus",
    llm_personality="default",
)

# ----------------------------------------------------------------------
# Mistral AI
# ----------------------------------------------------------------------

# Mistral 7B
altruistic_mistral_7b_agent = AgentConfig(
    name="Altruistic Mistral 7B",
    agent_type="llm",
    llm_model="open-mistral-7b",
    llm_personality="altruistic",
)

selfish_mistral_7b_agent = AgentConfig(
    name="Selfish Mistral 7B",
    agent_type="llm",
    llm_model="open-mistral-7b",
    llm_personality="selfish",
)

default_mistral_7b_agent = AgentConfig(
    name="Default Mistral 7B",
    agent_type="llm",
    llm_model="open-mistral-7b",
    llm_personality="default",
)

# Mixtral 8x7B
altruistic_mixtral_8x7b_agent = AgentConfig(
    name="Altruistic Mixtral 8x7B",
    agent_type="llm",
    llm_model="open-mixtral-8x7b",
    llm_personality="altruistic",
)

selfish_mixtral_8x7b_agent = AgentConfig(
    name="Selfish Mixtral 8x7B",
    agent_type="llm",
    llm_model="open-mixtral-8x7b",
    llm_personality="selfish",
)

default_mixtral_8x7b_agent = AgentConfig(
    name="Default Mixtral 8x7B",
    agent_type="llm",
    llm_model="open-mixtral-8x7b",
    llm_personality="default",
)

# Mixtral 8x22B
altruistic_mixtral_8x22b_agent = AgentConfig(
    name="Altruistic Mixtral 8x22B",
    agent_type="llm",
    llm_model="open-mixtral-8x22b",
    llm_personality="altruistic",
)

selfish_mixtral_8x22b_agent = AgentConfig(
    name="Selfish Mixtral 8x22B",
    agent_type="llm",
    llm_model="open-mixtral-8x22b",
    llm_personality="selfish",
)

default_mixtral_8x22b_agent = AgentConfig(
    name="Default Mixtral 8x22B",
    agent_type="llm",
    llm_model="open-mixtral-8x22b",
    llm_personality="default",
)

# Mistral Small
altruistic_mistral_small_agent = AgentConfig(
    name="Altruistic Mistral Small",
    agent_type="llm",
    llm_model="mistral-small-latest",
    llm_personality="altruistic",
)

selfish_mistral_small_agent = AgentConfig(
    name="Selfish Mistral Small",
    agent_type="llm",
    llm_model="mistral-small-latest",
    llm_personality="selfish",
)

default_mistral_small_agent = AgentConfig(
    name="Default Mistral Small",
    agent_type="llm",
    llm_model="mistral-small-latest",
    llm_personality="default",
)

# Mistral Medium
altruistic_mistral_medium_agent = AgentConfig(
    name="Altruistic Mistral Medium",
    agent_type="llm",
    llm_model="mistral-medium-latest",
    llm_personality="altruistic",
)

selfish_mistral_medium_agent = AgentConfig(
    name="Selfish Mistral Medium",
    agent_type="llm",
    llm_model="mistral-medium-latest",
    llm_personality="selfish",
)

default_mistral_medium_agent = AgentConfig(
    name="Default Mistral Medium",
    agent_type="llm",
    llm_model="mistral-medium-latest",
    llm_personality="default",
)

# Mistral Large
altruistic_mistral_large_agent = AgentConfig(
    name="Altruistic Mistral Large",
    agent_type="llm",
    llm_model="mistral-large-latest",
    llm_personality="altruistic",
)

selfish_mistral_large_agent = AgentConfig(
    name="Selfish Mistral Large",
    agent_type="llm",
    llm_model="mistral-large-latest",
    llm_personality="selfish",
)

default_mistral_large_agent = AgentConfig(
    name="Default Mistral Large",
    agent_type="llm",
    llm_model="mistral-large-latest",
    llm_personality="default",
)

# ----------------------------------------------------------------------
# GOOGLE
# ----------------------------------------------------------------------

# Configurations for Gemini-1.0-Pro

altruistic_gemini_1_pro_agent = AgentConfig(
    name="Altruistic Gemini 1.0 Pro",
    agent_type="llm",
    llm_model="gemini-1.0-pro",
    llm_personality="altruistic",
)

selfish_gemini_1_pro_agent = AgentConfig(
    name="Selfish Gemini 1.0 Pro",
    agent_type="llm",
    llm_model="gemini-1.0-pro",
    llm_personality="selfish",
)

default_gemini_1_pro_agent = AgentConfig(
    name="Default Gemini 1.0 Pro",
    agent_type="llm",
    llm_model="gemini-1.0-pro",
    llm_personality="default",
)
