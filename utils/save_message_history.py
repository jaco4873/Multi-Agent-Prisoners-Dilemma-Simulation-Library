import os
import datetime
from utils.sanitize_file_name import sanitize_filename


def save_message_history(agent, opponent_name, directory):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d-%H:%M")
    filename = (
        sanitize_filename(f"{agent.config.name}_message_history_{formatted_time}")
        + ".txt"
    )
    file_path = os.path.join(directory, filename)

    message_type_mapping = {
        "langchain_core.messages.ai.AIMessage": "Agent",
        "langchain_core.messages.system.SystemMessage": "System",
        "langchain_core.messages.human.HumanMessage": "GameMaster",
    }

    try:
        with open(file_path, "w") as file:
            separator = "-" * 80
            file.write(
                f"LLM history for {agent.config.name} playing against {opponent_name}\n\n"
            )
            file.write(separator + "\n\n")

            for message in agent.llm_messages:
                # Check message type and content
                class_name = type(message).__module__ + "." + type(message).__name__

                message_label = message_type_mapping.get(
                    class_name, "Unknown Message Type"
                )
                message_content = message.content

                file.write(f"Type: {message_label}\nContent: {message_content}\n\n")
                file.write(separator + "\n\n")

        print(f"Message history saved successfully as {filename}")
    except Exception as e:
        print(f"Error during file operation: {e}")
