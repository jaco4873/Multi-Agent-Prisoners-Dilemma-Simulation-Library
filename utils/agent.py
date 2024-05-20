import random
import re
import os
from models.agent_config import AgentConfig
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv


from prompts.personalities.custom_personality_message import custom_personality_message
from prompts.personalities.selfish_personality_message import (
    selfish_personality_message,
)
from prompts.personalities.altruistic_personality_message import (
    altruistic_personality_message,
)
from prompts.game_description import game_description

load_dotenv


class Agent:
    """
    Represents an agent in a Prisoner's Dilemma game.

    Attributes:
        config (AgentConfig): Configuration settings for the agent.
        role (str): The role of the agent ('Agent A' or 'Agent B').
        llm_messages (list): List of messages exchanged with the language learning model.
        choice_prompt (str): The prompt for the agent's decision.
        score (int): The current score of the agent.

    Methods:
        __init__: Initializes a new instance of the Agent class.
        decide_action: Determines the action to be taken by the agent based on its type.
        get_decision_fixed_agent: Executes the fixed strategy of the agent to decide an action.
        get_decision_human_agent: Collects a decision input from a human user through the console.
        get_decision_llm_agent: Utilizes a language model to determine the agent's decision.
        query_llm: Queries a language learning model to get a decision based on the game's history.
        get_llm_client: Gets the appropriate language learning model client based on the configured model.
        extract_decision: Extracts the decision from the given response string.
        update_score: Updates the agent's score based on the outcome of the last round in a Prisoner's Dilemma game.
    """

    def __init__(self, config: AgentConfig, role: str, choice_prompt: str):
        """
        Initializes a new instance of the Agent class.

        Args:
            config (AgentConfig): Configuration settings for the agent.
            role (str): The role of the agent ('Agent A' or 'Agent B').
            choice_prompt (str): The prompt for the agent's decision.
        """
        self.config = config
        self.role = role
        self.llm_messages = []
        self.choice_prompt = choice_prompt
        self.score = 0

    def decide_action(self, game_history, opponent_score):
        """
        Determines the action to be taken by the agent based on its type.

        Returns:
            str: The decision of the agent ('COOPERATE' or 'DEFECT').

        Raises:
            ValueError: If an unknown agent type is provided in the configuration.
        """
        if self.config.agent_type == "fixed":
            return self.get_decision_fixed_agent(game_history)
        elif self.config.agent_type == "human":
            return self.get_decision_human_agent()
        elif self.config.agent_type == "llm":
            return self.get_decision_llm_agent(game_history, opponent_score)

    def get_decision_fixed_agent(self, game_history):
        """
        Executes the fixed strategy of the agent to decide an action.

        Returns:
            str: The decision of the agent based on a predefined strategy.

        Raises:
            ValueError: If no fixed strategy is set in the configuration.
        """
        if not self.config.fixed_strategy:
            raise ValueError("Fixed strategy not set")

        opponent_role = "Agent B" if self.role == "Agent A" else "Agent A"
        opponent_history = [
            round[opponent_role] for round in game_history if opponent_role in round
        ]
        return self.config.fixed_strategy(opponent_history)

    def get_decision_human_agent(self):
        """
        Collects a decision input from a human user through the console.

        Returns:
            str: The validated input from the user, either 'COOPERATE' or 'DEFECT'.

        Notes:
            Continuously prompts until a valid input is received.
        """
        valid_choices = ["C", "D"]
        while True:
            user_input = input("Enter your decision (C/D):")
            if user_input.strip().upper() in valid_choices:
                if user_input.strip().upper() == "C":
                    return "COOPERATE"
                else:
                    return "DEFECT"
            else:
                print("Invalid input. Please enter 'C' or 'D'.")

    def get_decision_llm_agent(self, game_history, opponent_score):
        """
        Utilizes a language model to determine the agent's decision.

        Returns:
            str: The decision inferred from the language model response.

        Notes:
            Defaults to a random choice if no model is configured.
        """
        response = self.query_llm(game_history, opponent_score)
        decision = self.extract_decision(response)
        return decision

    def query_llm(self, game_history, opponent_score):
        """
        Queries a language learning model to get a decision based on the game's history.

        Returns:
            str: The content received from the model's response.

        Raises:
            ValueError: If the personality is not set for an LLM agent type.
            Exception: General exceptions are re-raised after logging.
        """

        personality_prompts = {
            "selfish": selfish_personality_message,
            "altruistic": altruistic_personality_message,
            "custom": custom_personality_message,
            "default": " ",
        }

        llm = self.get_llm_client()

        if len(game_history) == 0:
            self.llm_messages.append(
                SystemMessage(
                    content=game_description
                    + "\n"
                    + personality_prompts[self.config.llm_personality]
                )
            )

        if len(game_history) > 0:
            opponent_role = "Agent B" if self.role == "Agent A" else "Agent A"
            self.llm_messages.append(
                HumanMessage(
                    content=(
                        "Your opponent chose to "
                        + str(game_history[-1][opponent_role])
                        + "\nThe new score is: You: "
                        + str(self.score)
                        + " Opponent: "
                        + str(opponent_score)
                        + "."
                    )
                )
            )

        self.llm_messages.append(HumanMessage(content=self.choice_prompt))

        try:
            api_response = llm.invoke(self.llm_messages)

            self.llm_messages.append(api_response)

            str_response = str(api_response.content)

            return str_response

        except Exception as e:
            print(f"Error: {e}")
            raise

    def get_llm_client(self):
        model = self.config.llm_model

        if model in ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o"]:
            llm = ChatOpenAI(
                model=model,
                temperature=os.environ["LLM_TEMPERATURE"],
                openai_api_key=os.environ["OPENAI_API_KEY"],
            )

        elif model in [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ]:
            llm = ChatAnthropic(
                model=model,
                temperature=os.environ["LLM_TEMPERATURE"],
                anthropic_api_key=os.environ["ANTHROPIC_API_KEY"],
            )

        elif model in ["gemini-1.0-pro", "gemini-1.5-pro-latest"]:
            llm = ChatGoogleGenerativeAI(
                model=model,
                temperature=os.environ["LLM_TEMPERATURE"],
                google_api_key=os.environ["GOOGLE_API_KEY"],
                convert_system_message_to_human=True,
            )

        elif model in ["command", "command-light", "command-r", "command-r-plus"]:
            llm = ChatCohere(
                model=model,
                temperature=os.environ["LLM_TEMPERATURE"],
                cohere_api_key=os.environ["COHERE_API_KEY"],
            )

        elif model in [
            "open-mistral-7b",
            "open-mixtral-8x7b",
            "open-mixtral-8x22b",
            "mistral-small-latest",
            "mistral-medium-latest",
            "mistral-large-latest",
        ]:
            llm = ChatMistralAI(
                model=model,
                temperature=os.environ["LLM_TEMPERATURE"],
                mistral_api_key=os.environ["MISTRAL_API_KEY"],
            )

        else:
            raise ValueError(
                f"Invalid model name: {model}. Check supported models in the docs."
            )

        return llm

    def extract_decision(self, response):
        """
        Extracts the decision from the given response string using regular expressions,
        specifically retrieving the last occurrence of 'COOPERATE' or 'DEFECT'.

        Args:
            response (str): The raw response string from an LLM query.

        Returns:
            str: The last 'COOPERATE' or 'DEFECT' found in the response; defaults to a random choice if no match is found.
        """
        matches = re.findall(r"COOPERATE|DEFECT", response)
        return matches[-1] if matches else random.choice(["COOPERATE", "DEFECT"])

    def update_score(self, own_action, opponents_action):
        """
        Updates the agent's score based on the outcome of the last round in a Prisoner's Dilemma game.

        Args:

            own_action (str): The action taken by the agent in the last round ('COOPERATE' or 'DEFECT'

            opponents_action (str): The action taken by the other agent in the last round ('COOPERATE' or 'DEFECT').

        Raises:
            ValueError: If the history is empty, which implies that there's no previous action to reference, or if the agent's name does not exist in the last entry of the history.

        Notes:
            This method directly modifies the `score` attribute of the agent based on the outcome of the interactions as per the rules of the Prisoner's Dilemma. The score changes are logged to the console.
        """

        try:
            coop_coop_score = int(os.environ["COOPERATE_COOPERATE_SCORE"])
            coop_def_score = int(os.environ["COOPERATE_DEFECT_SCORE"])
            def_coop_score = int(os.environ["DEFECT_COOPERATE_SCORE"])
            def_def_score = int(os.environ["DEFECT_DEFECT_SCORE"])

        except KeyError as e:
            raise KeyError(f"Missing required environment variable: {e}")

        except ValueError as e:
            raise ValueError(f"Invalid value for environment variable: {e}")

        score_map = {
            ("COOPERATE", "COOPERATE"): coop_coop_score,
            ("COOPERATE", "DEFECT"): coop_def_score,
            ("DEFECT", "COOPERATE"): def_coop_score,
            ("DEFECT", "DEFECT"): def_def_score,
        }

        action_pair = (own_action, opponents_action)
        self.score += score_map[action_pair]

        print(f"New score for {self.config.name}: {self.score}")
