import random
import re
from models.agent_config import AgentConfig
from openai import OpenAI

from prompts.personalities.custom_personality_message import custom_personality_message
from prompts.personalities.selfish_personality_message import selfish_personality_message
from prompts.personalities.altruistic_personality_message import altruistic_personality_message
from prompts.game_description import game_description

class Agent:
    """
    Represents an agent in the Prisoner's Dilemma game.

    Attributes:
        config (AgentConfig): The configuration object for the agent.

    Methods:
        __init__(self, config: AgentConfig): Initializes the Agent object.
        decide_action(self): Makes a decision on the next action to take.
        get_decision_fixed_agent(self): Gets the decision for a fixed agent.
        get_decision_human_agent(self): Gets the decision for a human agent.
        get_decision_llm_agent(self): Gets the decision for an LLM agent.
        query_llm(self): Queries the LLM model for a decision.
        extract_decision(self, response): Extracts the decision from the LLM response.
        log_decision(self, response): Logs the LLM response to a file.
    """

    def __init__(self, config: AgentConfig, role: str, choice_prompt: str):
        """
        Initializes a new instance of the Agent class.

        Args:
            config (AgentConfig): Configuration settings for the agent.
            role (str): The role of the agent ('Agent A' or 'Agent B').
        """
        self.config = config
        self.role = role
        self.llm_messages = []
        self.choice_prompt = choice_prompt

    def decide_action(self, game_history, opponent_score):
        """
        Determines the action to be taken by the agent based on its type.

        Returns:
            str: The decision of the agent ('COOPERATE' or 'DEFECT').

        Raises:
            ValueError: If an unknown agent type is provided in the configuration.
        """
        if self.config.agent_type == 'fixed':
            return self.get_decision_fixed_agent(game_history)
        elif self.config.agent_type == 'human':
            return self.get_decision_human_agent()
        elif self.config.agent_type == 'llm':
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
        
        opponent_role = 'Agent B' if self.role == 'Agent A' else 'Agent A'
        opponent_history = [round[opponent_role] for round in game_history if opponent_role in round]
        return self.config.fixed_strategy(opponent_history)
    
        
    def get_decision_human_agent(self):
        """
        Collects a decision input from a human user through the console.

        Returns:
            str: The validated input from the user, either 'COOPERATE' or 'DEFECT'.

        Notes:
            Continuously prompts until a valid input is received.
        """
        valid_choices = ["COOPERATE", "DEFECT"]
        while True:
            user_input = input("Enter your decision (COOPERATE/DEFECT): ")
            if user_input.strip().upper() in valid_choices:
                return user_input.strip().upper() 
            else:
                print("Invalid input. Please enter 'COOPERATE' or 'DEFECT'.")

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
        self.log_decision(response)
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
        if self.config.llm_model in ['gpt-3.5-turbo', 'gpt-4-turbo']:
            client = OpenAI()
        
        personality_prompts = {
            'selfish': selfish_personality_message,
            'altruistic': altruistic_personality_message,
            'custom': custom_personality_message
        }
        

        if len(game_history) == 0:
            self.llm_messages.append({"role": "system", "content": game_description + '\n\n'  + personality_prompts[self.config.llm_personality]})
        
        if len(game_history) > 0:
            opponent_role = 'Agent B' if self.role == 'Agent A' else 'Agent A'
            self.llm_messages.append({
                "role": "user",
                "content": (
                    "Your opponent chose to " + str(game_history[-1][opponent_role]) +
                    "'\n\n' The new score is: You: " + str(self.config.score) + " Opponent: " + str(opponent_score) + "."
                )
            })
        
        self.llm_messages.append({"role": "user", "content": self.choice_prompt})
        
        try:
            response = client.chat.completions.create(
                model = self.config.llm_model,
                messages=self.llm_messages
            )
            
            self.llm_messages.append({"role": "assistant", "content": response.choices[0].message.content})
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error: {e}")
            raise

    def extract_decision(self, response):
        """
        Extracts the decision from the given response string using regular expressions,
        specifically retrieving the last occurrence of 'COOPERATE' or 'DEFECT'.

        Args:
            response (str): The raw response string from an LLM query.

        Returns:
            str: The last 'COOPERATE' or 'DEFECT' found in the response; defaults to a random choice if no match is found.
        """
        matches = re.findall(r'COOPERATE|DEFECT', response)
        return matches[-1] if matches else random.choice(["COOPERATE", "DEFECT"])

    def log_decision(self, response):
        """
        Logs the decision response to a file.

        Args:
            response (str): The response to be logged.

        Notes:
            Appends the response to 'llm_log.txt' with a separator for clarity.
        """
        with open("llm_log.txt", 'a') as log_file:
            log_file.write(f"{response}\n-----------------------------------------------------------------------\n")
            
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

        score_map = {
            ('COOPERATE', 'COOPERATE'): 3,  # Mutual cooperation
            ('COOPERATE', 'DEFECT'): 0,     # You cooperate, other defect
            ('DEFECT', 'COOPERATE'): 5,     # You defect, other cooperate
            ('DEFECT', 'DEFECT'): 1         # Mutual defection
        }

        action_pair = (own_action, opponents_action)
        self.config.score += score_map[action_pair]

        print(f"New score for {self.config.name}: {self.config.score}")
