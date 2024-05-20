import csv
import os
import datetime


def write_simulation_results(results, directory="data/all_matchups_results"):
    """
    Writes the simulation results to a CSV file.

    Parameters:
    - results: List of tuples containing the results.
    - directory: The directory where the CSV file will be saved.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results-{formatted_time}.csv" 
    filepath = os.path.join(directory, filename)

    total_score_a = 0
    total_score_b = 0

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Agent A", "Score A", "Agent B", "Score B"])
        for result in results:
            writer.writerow(result)
            total_score_a += result[1]
            total_score_b += result[3]

        writer.writerow(["TOTAL OUTRIGHT", total_score_a, "", total_score_b])
        writer.writerow(
            [
                "TOTAL ADJUSTED",
                total_score_a - total_score_b,
                "",
                total_score_b - total_score_a,
            ]
        )

    print(f"Simulation results saved to {filepath}")
