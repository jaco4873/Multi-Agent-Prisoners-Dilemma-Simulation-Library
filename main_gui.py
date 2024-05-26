import os
import sys
import tkinter as tk
import threading
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from dotenv import load_dotenv, set_key
from utils.simulation import simulate_prisoners_dilemma
from utils.write_simulation_overview import write_simulation_overview

# Import agents
from agent_configs.human_agent_config import human_agent
from agent_configs.llm_agent_configs import (
    altruistic_gpt_4_omni_agent,
    selfish_gpt_4_omni_agent,
    default_gpt_4_omni_agent,
    altruistic_gpt_4_turbo_agent,
    selfish_gpt_4_turbo_agent,
    default_gpt_4_turbo_agent,
    altruistic_gpt_4_agent,
    selfish_gpt_4_agent,
    default_gpt_4_agent,
    altruistic_gpt_35_turbo_agent,
    selfish_gpt_35_turbo_agent,
    default_gpt_35_turbo_agent,
    altruistic_claude3_opus_agent,
    selfish_claude3_opus_agent,
    default_claude3_opus_agent,
    altruistic_claude3_sonnet_agent,
    selfish_claude3_sonnet_agent,
    default_claude3_sonnet_agent,
    altruistic_claude3_haiku_agent,
    selfish_claude3_haiku_agent,
    default_claude3_haiku_agent,
    altruistic_command_agent,
    selfish_command_agent,
    default_command_agent,
    altruistic_command_light_agent,
    selfish_command_light_agent,
    default_command_light_agent,
    altruistic_command_r_agent,
    selfish_command_r_agent,
    default_command_r_agent,
    altruistic_command_r_plus_agent,
    selfish_command_r_plus_agent,
    default_command_r_plus_agent,
    altruistic_mistral_7b_agent,
    selfish_mistral_7b_agent,
    default_mistral_7b_agent,
    altruistic_mixtral_8x7b_agent,
    selfish_mixtral_8x7b_agent,
    default_mixtral_8x7b_agent,
    altruistic_mixtral_8x22b_agent,
    selfish_mixtral_8x22b_agent,
    default_mixtral_8x22b_agent,
    altruistic_mistral_small_agent,
    selfish_mistral_small_agent,
    default_mistral_small_agent,
    altruistic_mistral_medium_agent,
    selfish_mistral_medium_agent,
    default_mistral_medium_agent,
    altruistic_mistral_large_agent,
    selfish_mistral_large_agent,
    default_mistral_large_agent,
    altruistic_gemini_1_pro_agent,
    selfish_gemini_1_pro_agent,
    default_gemini_1_pro_agent,
)

from agent_configs.fixed_strategy_agent_configs import (
    tit_for_tat_agent,
    suspicious_tit_for_tat_agent,
    forgiving_tit_for_tat_agent,
    defection_sensitive_tit_for_tat_agent,
    tit_for_two_tats_agent,
    grim_trigger_agent,
    always_cooperate_agent,
    adaptive_strategy_agent,
    soft_majority_agent,
    hard_majority_agent,
    random_strategy_agent,
    betrayal_agent,
)
from prompts.choice_prompts.choice_prompt_without_reasoning import (
    choice_prompt_without_reasoning,
)
from prompts.choice_prompts.choice_prompt_with_reasoning import (
    choice_prompt_with_reasoning,
)

from prompts.choice_prompts.choice_prompt_custom import choice_prompt_custom

# Dictionairy for the choice prompts
choice_prompts = {
    "Chain of Thought Reasoning": choice_prompt_with_reasoning,
    "Decision only": choice_prompt_without_reasoning,
    "Custom prompt": choice_prompt_custom,
}

# Dictionary mapping agent names to agent configs
agent_dict = {
    "Human Participant": human_agent,
    "GPT-4 Omni Altruistic": altruistic_gpt_4_omni_agent,
    "GPT-4 Omni Selfish": selfish_gpt_4_omni_agent,
    "GPT-4 Omni Default": default_gpt_4_omni_agent,
    "GPT-4 Turbo Altruistic": altruistic_gpt_4_turbo_agent,
    "GPT-4 Turbo Selfish": selfish_gpt_4_turbo_agent,
    "GPT-4 Turbo Default": default_gpt_4_turbo_agent,
    "GPT-4 Altruistic": altruistic_gpt_4_agent,
    "GPT-4 Selfish": selfish_gpt_4_agent,
    "GPT-4 Default": default_gpt_4_agent,
    "GPT-3.5 Turbo Altruistic": altruistic_gpt_35_turbo_agent,
    "GPT-3.5 Turbo Selfish": selfish_gpt_35_turbo_agent,
    "GPT-3.5 Turbo Default": default_gpt_35_turbo_agent,
    "Claude 3 Opus Altruistic": altruistic_claude3_opus_agent,
    "Claude 3 Opus Selfish": selfish_claude3_opus_agent,
    "Claude 3 Opus Default": default_claude3_opus_agent,
    "Claude 3 Sonnet Altruistic": altruistic_claude3_sonnet_agent,
    "Claude 3 Sonnet Selfish": selfish_claude3_sonnet_agent,
    "Claude 3 Sonnet Default": default_claude3_sonnet_agent,
    "Claude 3 Haiku Altruistic": altruistic_claude3_haiku_agent,
    "Claude 3 Haiku Selfish": selfish_claude3_haiku_agent,
    "Claude 3 Haiku Default": default_claude3_haiku_agent,
    "Command Altruistic": altruistic_command_agent,
    "Command Selfish": selfish_command_agent,
    "Command Default": default_command_agent,
    "Command Light Altruistic": altruistic_command_light_agent,
    "Command Light Selfish": selfish_command_light_agent,
    "Command Light Default": default_command_light_agent,
    "Command R Altruistic": altruistic_command_r_agent,
    "Command R Selfish": selfish_command_r_agent,
    "Command R Default": default_command_r_agent,
    "Command R Plus Altruistic": altruistic_command_r_plus_agent,
    "Command R Plus Selfish": selfish_command_r_plus_agent,
    "Command R Plus Default": default_command_r_plus_agent,
    "Mistral 7B Altruistic": altruistic_mistral_7b_agent,
    "Mistral 7B Selfish": selfish_mistral_7b_agent,
    "Mistral 7B Default": default_mistral_7b_agent,
    "Mixtral 8x7B Altruistic": altruistic_mixtral_8x7b_agent,
    "Mixtral 8x7B Selfish": selfish_mixtral_8x7b_agent,
    "Mixtral 8x7B Default": default_mixtral_8x7b_agent,
    "Mixtral 8x22B Altruistic": altruistic_mixtral_8x22b_agent,
    "Mixtral 8x22B Selfish": selfish_mixtral_8x22b_agent,
    "Mixtral 8x22B Default": default_mixtral_8x22b_agent,
    "Mistral Small Altruistic": altruistic_mistral_small_agent,
    "Mistral Small Selfish": selfish_mistral_small_agent,
    "Mistral Small Default": default_mistral_small_agent,
    "Mistral Medium Altruistic": altruistic_mistral_medium_agent,
    "Mistral Medium Selfish": selfish_mistral_medium_agent,
    "Mistral Medium Default": default_mistral_medium_agent,
    "Mistral Large Altruistic": altruistic_mistral_large_agent,
    "Mistral Large Selfish": selfish_mistral_large_agent,
    "Mistral Large Default": default_mistral_large_agent,
    "Gemini 1 Pro Altruistic": altruistic_gemini_1_pro_agent,
    "Gemini 1 Pro Selfish": selfish_gemini_1_pro_agent,
    "Gemini 1 Pro Default": default_gemini_1_pro_agent,
    "Tit for Tat": tit_for_tat_agent,
    "Suspicious Tit for Tat": suspicious_tit_for_tat_agent,
    "Forgiving Tit for Tat": forgiving_tit_for_tat_agent,
    "Defection Sensitive Tit for Tat": defection_sensitive_tit_for_tat_agent,
    "Tit for Two Tats": tit_for_two_tats_agent,
    "Grim Trigger": grim_trigger_agent,
    "Always Cooperate": always_cooperate_agent,
    "Adaptive Strategy": adaptive_strategy_agent,
    "Soft Majority": soft_majority_agent,
    "Hard Majority": hard_majority_agent,
    "Random Strategy": random_strategy_agent,
    "Betrayal": betrayal_agent,
}

class ConsoleOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


class GUIInputHandler:
    def __init__(self, root, status_label):
        self.root = root
        self.input_queue = []
        self.ready = False
        self.status_label = status_label

    def read(self):
        self.ready = False
        self.status_label.config(
            text="Please make your decision using the buttons above."
        )
        while not self.ready:
            self.root.update()
            self.root.after(100)
        self.status_label.config(text="")
        return self.input_queue.pop(0)

    def readline(self):
        return self.read()

    def write(self, s):
        pass

    def flush(self):
        pass

    def input_received(self, value):
        self.input_queue.append(value)
        self.ready = True


def setup_gui_input(root):
    status_label = ttk.Label(root, text="", font=("Helvetica", 14))
    status_label.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
    input_handler = GUIInputHandler(root, status_label)
    sys.stdin = input_handler
    return input_handler


def add_decision_buttons(console_frame, input_handler):
    overlay_frame = ttk.Frame(console_frame)
    overlay_frame.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    ttk.Button(
        overlay_frame,
        text="COOPERATE",
        command=lambda: input_handler.input_received("C"),
    ).grid(row=0, column=0, padx=5)

    ttk.Button(
        overlay_frame,
        text="DEFECT",
        command=lambda: input_handler.input_received("D"),
    ).grid(row=0, column=1, padx=5)


def filter_combobox(event, combobox, values):
    typed_text = combobox.get()
    if typed_text == "":
        combobox["values"] = values
    else:
        filtered_values = [
            value for value in values if typed_text.lower() in value.lower()
        ]
        combobox["values"] = filtered_values


def clear_placeholder(event, combobox, placeholder):
    if combobox.get() == placeholder:
        combobox.set("")


def restore_placeholder(event, combobox, placeholder):
    if combobox.get() == "":
        combobox.set(placeholder)


def add_matchup():
    frame = ttk.Frame(scrollable_matchups_frame)
    frame.grid(padx=5, pady=5, sticky="ew")

    # Agent selection dropdowns
    agent_names = list(agent_dict.keys())
    config_a = ttk.Combobox(frame, values=agent_names, width=20)
    config_a.grid(row=0, column=0, padx=5, pady=5)
    placeholder_a = "Select Agent A"
    config_a.set(placeholder_a)
    config_a.bind(
        "<KeyRelease>", lambda event: filter_combobox(event, config_a, agent_names)
    )
    config_a.bind(
        "<FocusIn>",
        lambda event, c=config_a, p=placeholder_a: clear_placeholder(event, c, p),
    )
    config_a.bind(
        "<FocusOut>",
        lambda event, c=config_a, p=placeholder_a: restore_placeholder(event, c, p),
    )

    config_b = ttk.Combobox(frame, values=agent_names, width=20)
    config_b.grid(row=0, column=1, padx=5, pady=5)
    placeholder_b = "Select Agent B"
    config_b.set(placeholder_b)
    config_b.bind(
        "<KeyRelease>", lambda event: filter_combobox(event, config_b, agent_names)
    )
    config_b.bind(
        "<FocusIn>",
        lambda event, c=config_b, p=placeholder_b: clear_placeholder(event, c, p),
    )
    config_b.bind(
        "<FocusOut>",
        lambda event, c=config_b, p=placeholder_b: restore_placeholder(event, c, p),
    )

    # Remove button for matchups
    remove_lbl = ttk.Label(frame, text="\u274c", font=("Helvetica", 16))
    remove_lbl.grid(row=0, column=2, padx=5, pady=5)
    remove_lbl.bind("<Button-1>", lambda event: remove_matchup(frame))

    matchups_frames.append((frame, config_a, config_b))


def remove_matchup(frame):
    for i, (f, config_a, config_b) in enumerate(matchups_frames):
        if f == frame:
            matchups_frames.pop(i)
            frame.destroy()
            break


def add_choice_prompt_selection(root, choice_prompts):
    frame = ttk.Frame(root)
    frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    label = ttk.Label(frame, text="Select Choice Prompt:")
    label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    choice_prompt_var = tk.StringVar()
    choice_prompt_dropdown = ttk.Combobox(
        frame,
        textvariable=choice_prompt_var,
        values=list(choice_prompts.keys()),
        state="readonly",
    )
    choice_prompt_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    choice_prompt_dropdown.set("Chain of Thought Reasoning")

    return choice_prompt_var


def run_simulation():
    load_dotenv()
    iterations = int(os.getenv("ITERATIONS", 10))  # Default to 10 if not set

    selected_prompt_key = choice_prompt_var.get()
    if selected_prompt_key == "Custom prompt":
        choice_prompt = custom_prompt_text.get("1.0", tk.END).strip()
    else:
        choice_prompt = choice_prompts[selected_prompt_key]

    matchups = []
    for frame, config_a, config_b in matchups_frames:
        agent_a = config_a.get()
        agent_b = config_b.get()
        if agent_a != "Select Agent A" and agent_b != "Select Agent B":
            matchups.append((agent_dict[agent_a], agent_dict[agent_b]))

    if not matchups:
        messagebox.showerror("Error", "Please configure at least one valid matchup.")
        return

    def simulation_thread():
        results = []
        for config_a, config_b in matchups:
            print(f"Running simulation: {config_a.name} vs {config_b.name}")
            simulation_results = simulate_prisoners_dilemma(
                config_a, config_b, iterations, choice_prompt
            )
            results.append(simulation_results)
            
        write_simulation_overview(results)

        messagebox.showinfo(
            "Simulation Completed",
            "Simulation Completed Successfully. Find the results in the data folder.",
        )

    thread = threading.Thread(target=simulation_thread)
    thread.start()


def update_env(var, value):
    os.environ[var] = value
    set_key(".env", var, value)


def add_settings_group(
    settings_frame, group_name, env_vars, start_row, choice_prompt_var=None
):
    header = ttk.Label(settings_frame, text=group_name, font=("Helvetica", 14, "bold"))
    header.grid(row=start_row, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")

    current_row = start_row + 1
    for var, label in env_vars.items():
        lbl = ttk.Label(settings_frame, text=label)
        lbl.grid(row=current_row, column=0, padx=5, pady=5, sticky="w")

        if var == "CHOICE_PROMPT" and choice_prompt_var:
            choice_prompt_dropdown = ttk.Combobox(
                settings_frame,
                textvariable=choice_prompt_var,
                values=list(choice_prompts.keys()),
                state="readonly",
            )
            choice_prompt_dropdown.grid(
                row=current_row, column=1, padx=5, pady=5, sticky="ew"
            )
            choice_prompt_dropdown.set("Chain of Thought Reasoning")
        else:
            ent = ttk.Entry(settings_frame)
            ent.grid(row=current_row, column=1, padx=5, pady=5, sticky="ew")
            ent.insert(
                0, os.getenv(var, "")
            )  # Pre-fill with current value if available
            ent.bind("<FocusOut>", lambda e, var=var: update_env(var, e.widget.get()))

        current_row += 1

    return current_row


def add_scrollable_frame(container):
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    scrollable_frame.bind_all("<MouseWheel>", on_mouse_wheel)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    return scrollable_frame


# Function to list files in a directory
def list_files(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith(extension)]


# Function to open selected file
def open_file(file_path):
    try:
        if file_path.endswith(".csv"):
            os.system(f"open {file_path}")  # Open CSV file with the default application
        else:
            os.system(f"open {file_path}")  # Open graph with the default application
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")


# Function to update file list
def update_file_list(treeview, directory, extension):
    for item in treeview.get_children():
        treeview.delete(item)
    files = list_files(directory, extension)
    for file in files:
        treeview.insert("", "end", text=file)


# ----------------------------------------------------------------------
# Creating the GUI
# ----------------------------------------------------------------------

# Creating the main window
root = tk.Tk()
root.title("Prisoner's Dilemma Simulator")

# Configure column weights for the main grid layout to set relative widths
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Configure row weights to ensure the proper distribution of space
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)

# Define the bold font and create a style object
bold_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
style = ttk.Style()
style.configure("Bold.TLabelframe.Label", font=bold_font)

# Set consistent background color for all frames
style.configure("TFrame")
style.configure("TLabelFrame")
style.configure("TLabel")
style.map("TLabelFrame", background=[("active", "!disabled")])
style.map(
    "Treeview",
    background=[["selected", "SystemHighlight"]],
    foreground=[("selected", "SystemWindowText")],
)

# ----------------
# COLUMN 1 
# ----------------

# Frame for settings
settings_outer_frame = ttk.Frame(root)
settings_outer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

settings_frame = ttk.LabelFrame(
    settings_outer_frame, text="Settings", style="Bold.TLabelframe"
)
settings_frame.pack(fill="both", expand=True)

scrollable_settings_frame = add_scrollable_frame(settings_frame)

# Grouping environment variables by category
general = {"ITERATIONS": "Iterations per Matchup"}

config = {
    "CHOICE_PROMPT": "Choice Prompt",
    "LLM_TEMPERATURE": "LLM Temperature",
}

api_keys = {
    "OPENAI_API_KEY": "OpenAI API Key",
    "ANTHROPIC_API_KEY": "Anthropic API Key",
    "GOOGLE_API_KEY": "Google API Key",
    "COHERE_API_KEY": "Cohere API Key",
    "MISTRAL_API_KEY": "Mistral API Key",
}

payoff_matrix_settings = {
    "COOPERATE_COOPERATE_SCORE": "Cooperate-Cooperate Score",
    "COOPERATE_DEFECT_SCORE": "Cooperate-Defect Score",
    "DEFECT_COOPERATE_SCORE": "Defect-Cooperate Score",
    "DEFECT_DEFECT_SCORE": "Defect-Defect Score",
}


# Adding settings groups
choice_prompt_var = tk.StringVar()


current_row = add_settings_group(scrollable_settings_frame, "General", general, 0)
current_row += 1  
current_row = add_settings_group(
    scrollable_settings_frame, "LLM Config", config, current_row, choice_prompt_var
)
current_row += 1  
current_row = add_settings_group(
    scrollable_settings_frame, "Payoff Matrix", payoff_matrix_settings, current_row
)
current_row += 1  
current_row = add_settings_group(
    scrollable_settings_frame, "API Keys", api_keys, current_row
)

# Frame for custom choice prompt
custom_prompt_frame = ttk.LabelFrame(
    root, text="Enter custom choice prompt", style="Bold.TLabelframe"
)

custom_prompt_frame.grid(row=1, column=0, padx=10, pady=10, sticky="sew")

custom_prompt_text = tk.Text(custom_prompt_frame, wrap="word")
custom_prompt_text.grid(row=0, column=0, padx=5, pady=5, sticky="sew")

# Load the default custom choice prompt
default_custom_prompt = choice_prompt_custom
custom_prompt_text.insert(tk.END, default_custom_prompt)

# ----------------
# COLUMN 2 
# ----------------

# Frame for matchups
matchups_outer_frame = ttk.Frame(root)
matchups_outer_frame.grid(
    row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=10, sticky="nsew"
)

matchups_frame = ttk.LabelFrame(
    matchups_outer_frame, text="Matchups", style="Bold.TLabelframe"
)
matchups_frame.pack(fill="both", expand=True)

scrollable_matchups_frame = add_scrollable_frame(matchups_frame)


# Frame for buttons
button_frame = ttk.Frame(scrollable_matchups_frame)
button_frame.grid(row=99, column=0, columnspan=3, pady=10)

# Button to add matchups
add_matchup_btn = ttk.Button(button_frame, text="Add Matchup", command=add_matchup)
add_matchup_btn.grid(row=0, column=0, padx=5)

# Button to run simulation
run_simulation_btn = ttk.Button(
    button_frame, text="Run Simulation", command=run_simulation
)
run_simulation_btn.grid(row=0, column=1, padx=5)

# Frame for console output
console_frame = ttk.LabelFrame(root, text="Console Output", style="Bold.TLabelframe")
console_frame.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="sew")

console_output = tk.Text(console_frame, wrap="word")
console_output.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Added overlay frame for decision buttons
overlay_frame = ttk.Frame(console_frame)
overlay_frame.place(relx=1.0, rely=1.0, anchor="se", x=-0, y=-0)

ttk.Button(
    overlay_frame,
    text="COOPERATE",
    command=lambda: input_handler.input_received("C"),
).grid(row=0, column=0, padx=5)

ttk.Button(
    overlay_frame,
    text="DEFECT",
    command=lambda: input_handler.input_received("D"),
).grid(row=0, column=1, padx=5)

# List to keep track of matchup frames
matchups_frames = []

# Initially add one matchup
add_matchup()


# Input handler for the GUI
input_handler = setup_gui_input(root)

# Redirect stdout to console output
sys.stdout = ConsoleOutput(console_output)


# ----------------
# COLUMN 3 
# ----------------

# Frame for file list
file_list_frame = ttk.LabelFrame(root, text="Files", style="Bold.TLabelframe")
file_list_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")
file_list_frame.grid_columnconfigure(0, weight=1)
file_list_frame.grid_rowconfigure(1, weight=1)
file_list_frame.grid_rowconfigure(4, weight=1)
file_list_frame.grid_rowconfigure(7, weight=1)

# CSV Files Treeview
csv_label = ttk.Label(
    file_list_frame, text="Simulation Files", font=("Helvetica", 14, "bold")
)
csv_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

csv_treeview = ttk.Treeview(file_list_frame)
csv_treeview.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Graphs Treeview
graphs_label = ttk.Label(
    file_list_frame, text="Simulation Graphs", font=("Helvetica", 14, "bold")
)
graphs_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

graphs_treeview = ttk.Treeview(file_list_frame)
graphs_treeview.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# LLM Message History Treeview
llm_label = ttk.Label(
    file_list_frame, text="LLM Message History", font=("Helvetica", 14, "bold")
)
llm_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

llm_treeview = ttk.Treeview(file_list_frame)
llm_treeview.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

# Bind double-click event to open files
csv_treeview.bind(
    "<Double-1>",
    lambda event: open_file(
        os.path.join(
            "data/datasets", csv_treeview.item(csv_treeview.selection()[0])["text"]
        )
    ),
)
graphs_treeview.bind(
    "<Double-1>",
    lambda event: open_file(
        os.path.join(
            "data/graphs", graphs_treeview.item(graphs_treeview.selection()[0])["text"]
        )
    ),
)
llm_treeview.bind(
    "<Double-1>",
    lambda event: open_file(
        os.path.join(
            "data/llm_message_history",
            llm_treeview.item(llm_treeview.selection()[0])["text"],
        )
    ),
)

# Update the file lists
update_file_list(csv_treeview, "data/datasets", ".csv")
update_file_list(
    graphs_treeview, "data/graphs", ".png"
) 
update_file_list(llm_treeview, "data/llm_message_history", ".txt")

# Start the Tkinter event loop
root.mainloop()
