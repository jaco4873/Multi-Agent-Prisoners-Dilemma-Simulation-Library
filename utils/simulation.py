import csv
import os
import datetime
from utils.sanitize_file_name import sanitize_filename
from utils.plot_strategy_score import plot_scores
from utils.save_message_history import save_message_history
from utils.agent import Agent
from models.agent_config import AgentConfig


def setup_directories(base_path="./data"):
    """Sets up necessary directories for storing simulation data."""
    try:
        data_directory = os.path.join(base_path, "datasets")
        graphs_directory = os.path.join(base_path, "graphs")
        llm_message_history_directory = os.path.join(base_path, "llm_message_history")

        # Attempt to create directories
        os.makedirs(data_directory, exist_ok=True)
        os.makedirs(graphs_directory, exist_ok=True)
        os.makedirs(llm_message_history_directory, exist_ok=True)

        return data_directory, graphs_directory, llm_message_history_directory

    except Exception as e:
        print(f"Failed to create directories: {e}")
        raise


def simulate_prisoners_dilemma(
    config_a: AgentConfig, config_b: AgentConfig, iterations: int, choice_prompt: str
):
    """Simulates the Prisoner's Dilemma game between two agents.

    Args:
        config_a (AgentConfig): The configuration for Agent A.
        config_b (AgentConfig): The configuration for Agent B.
        iterations (int): The number of iterations to simulate.
        choice_prompt (str): The prompt for the agents to make their choices.

    Returns:
        Tuple[str, int, str, int]: A tuple containing the names and scores of Agent A and Agent B.
    """
    # Initialize the agents
    agent_a = Agent(config_a, role="Agent A", choice_prompt=choice_prompt)
    agent_b = Agent(config_b, role="Agent B", choice_prompt=choice_prompt)

    game_history = []

    data_directory, graphs_directory, llm_message_history_directory = (
        setup_directories()
    )

    # Define path for saving the simulation logfile
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    filename = (
        sanitize_filename(
            f"matchup_{agent_a.config.name}_vs_{agent_b.config.name}_{formatted_time}"
        )
        + ".csv"
    )
    full_path = os.path.join(data_directory, filename)

    with open(full_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Agent Name", "Round", "Choice", "Score"])

        for i in range(iterations):
            agent_a_choice = agent_a.decide_action(
                game_history, opponent_score=agent_b.score
            )
            agent_b_choice = agent_b.decide_action(
                game_history, opponent_score=agent_a.score
            )
            print(
                f"Iteration {i+1}: {agent_a.config.name} chooses {agent_a_choice}, {agent_b.config.name} chooses {agent_b_choice}"
            )

            round_result = {"Agent A": agent_a_choice, "Agent B": agent_b_choice}
            game_history.append(round_result)

            agent_a.update_score(agent_a_choice, agent_b_choice)
            agent_b.update_score(agent_b_choice, agent_a_choice)

            # Log the choices and scores after each round
            writer.writerow([agent_a.config.name, i + 1, agent_a_choice, agent_a.score])
            writer.writerow([agent_b.config.name, i + 1, agent_b_choice, agent_b.score])

    if agent_a.config.agent_type == "llm":
        save_message_history(
            agent_a, agent_b.config.name, llm_message_history_directory
        )

    if agent_b.config.agent_type == "llm":
        save_message_history(
            agent_b, agent_a.config.name, llm_message_history_directory
        )

    plot_scores(full_path, graphs_directory)

    return agent_a.config.name, agent_a.score, agent_b.config.name, agent_b.score
