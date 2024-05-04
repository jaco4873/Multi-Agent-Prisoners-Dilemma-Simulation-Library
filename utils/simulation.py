import csv
import os
import datetime
from helper_functions.sanitize_file_name import sanitize_filename
from utils.agent import Agent
from models.agent_config import AgentConfig 


def simulate_prisoners_dilemma(config_a: AgentConfig, config_b: AgentConfig, iterations: int):
    # Dictionary to track the results of each type of outcome
    results = {
        "COOPERATE-COOPERATE": 0,
        "COOPERATE-DEFECT": 0,
        "DEFECT-COOPERATE": 0,
        "DEFECT-DEFECT": 0
    }
    
    game_history = []

    agent_a = Agent(config_a, role="Agent A")
    agent_b = Agent(config_b, role="Agent B")

    # Prepare to log CSV
    data_directory = os.path.join('..', 'data/datasets')
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    filename_base = f"sim_{agent_a.config.name}_vs_{agent_b.config.name}_{formatted_time}"
    filename = sanitize_filename(filename_base)
    
    with open(os.path.join(data_directory, f"{filename}.csv"), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Agent Name','Round','Choice','Score'])

        for i in range(iterations):
            agent_a_choice = agent_a.decide_action(game_history)
            agent_b_choice = agent_b.decide_action(game_history)
            print(f"Iteration {i}: Agent A chooses {agent_a_choice}, Agent B chooses {agent_b_choice}")

            round_result = {'Agent A': agent_a_choice, 'Agent B': agent_b_choice}
            game_history.append(round_result)

            # Update the results dictionary based on the choices
            key = f"{agent_a_choice}-{agent_b_choice}"
            if key in results:
                results[key] += 1

            agent_a.update_score(agent_a_choice, agent_b_choice)
            agent_b.update_score(agent_b_choice, agent_a_choice)

            # Log the choices and scores after each round
            writer.writerow([agent_a.config.name, i+1, agent_a_choice, agent_a.config.score])
            writer.writerow([agent_b.config.name, i+1, agent_b_choice, agent_b.config.score])

    pl
    
    return results
