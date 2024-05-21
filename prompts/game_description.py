import os

try:
    coop_def_score = os.environ["COOPERATE_DEFECT_SCORE"]
    def_coop_score = os.environ["DEFECT_COOPERATE_SCORE"]
    def_def_score = os.environ["DEFECT_DEFECT_SCORE"]
    coop_coop_score = os.environ["COOPERATE_COOPERATE_SCORE"]

except KeyError as e:
    raise KeyError(f"Missing required environment variable: {e}")

game_description = f"""
Welcome to the Iterated Prisoner's Dilemma Game! In this game, you will make a series of decisions across multiple rounds, choosing whether to COOPERATE or DEFECT in each interaction with another player. The outcome of your decisions will affect not only your own score but also that of your opponent, based on the following payoff matrix:

COOPERATE-DEFECT: If you cooperate and your opponent defects, you will score {coop_def_score} points while your opponent scores {def_coop_score} points.
DEFECT-COOPERATE: If you defect and your opponent cooperates, you will score {def_coop_score} points while your opponent scores {coop_def_score} points.
DEFECT-DEFECT: If both you and your opponent choose to defect, each of you will score {def_def_score} points.
COOPERATE-COOPERATE: If both you and your opponent cooperate, each of you will score {coop_coop_score} points.

The winner is the player with the highest score at the end of the game.
"""
