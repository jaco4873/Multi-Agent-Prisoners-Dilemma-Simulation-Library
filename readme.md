# Multi-Agent Prisoner's Dilemma Simulation Library

## Introduction

This repository contains a generalized code library designed to streamline the data collection process for Iterated Prisoner's Dilemma (IPD) simulations with various types of agents, including large language models (LLMs), fixed strategies, and human participants. The library facilitates easy setup and execution of experiments, making the study of LLM behavior more accessible to researchers with limited programming knowledge.

## Features

- **Support for Multiple Agents:** Human participants, fixed strategies, and 18 different LLMs from 5 providers.
- **Customizable Prompts:** Easily inject custom prompts into LLM agents.
- **Simulation Parameters:** Control simulation parameters including the payoff matrix and LLM temperature.
- **Graphical User Interface (GUI):** Simplifies the configuration and execution of simulations.
- **Automatic Data Logging and Visualization:** Facilitates analysis of simulation results.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaco4873/Multi-Agent-Prisoners-Dilemma-Simulation-Library.git
   cd Multi-Agent-Prisoners-Dilemma-Simulation-Library
   ```

2. Install the required dependencies: 
   ``` bash
   pip install -r requirements.txt
   ```

3. Setup the empty variables in the environment file

## Usage

### Script-based Execution

1. Open `main.py` and modify the `matchups` variable to set up your desired simulations.
2. Run the script:
   ```bash
   python main.py
   ```

### Graphical User Interface Execution
1. Run the main_gui.py script to launch the GUI:
    ```bash
    python main_gui.py
    ```
2. Use the GUI to configure and execute simulations, view progress, access logged data, and visualize results.

## Customizing Simulations
- Agent Configuration: Use predefined agents or create custom configurations using the agent_config class.
- Prompts: Customize game description, personality prompt, and choice prompt.
- Simulation Settings: Configure the number of iterations, payoff matrix, and LLM temperature in the environment file.

## Contributions

Contributions to enhance the library are welcome. Potential improvements include support for additional game theory scenarios, more LLMs and fixed strategies, advanced visualization tools, and improved scalability.

For any issues or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License.

## Acknowledgements

This library was developed as part of an academic project. Special thanks to all contributors and the research community for their valuable feedback.