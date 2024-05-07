import os
import datetime
from utils.sanitize_file_name import sanitize_filename


def save_message_history(agent, opponent_name, directory):
    
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d-%H:%M")
    filename = sanitize_filename(f"{agent.config.name}_message_history_{formatted_time}") + '.txt'
    file_path = os.path.join(directory, filename)
    
        
    with open(file_path, 'w') as file:
        
        separator = '-' * 80
        file.write(f"LLM history for {agent.config.name} playing against {opponent_name}\n\n")
        file.write(separator + "\n\n")
        
        for message in agent.llm_messages:
            message_str = ', '.join([f"{key}: {value}" for key, value in message.items()])
            file.write(message_str + "\n\n")
            file.write(separator + "\n\n")