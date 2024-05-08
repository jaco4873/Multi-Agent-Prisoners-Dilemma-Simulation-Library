import os

try:
    coop_def_score = os.environ['COOPERATE_DEFECT_SCORE']
    def_coop_score = os.environ['DEFECT_COOPERATE_SCORE']
    def_def_score = os.environ['DEFECT_DEFECT_SCORE']
    coop_coop_score = os.environ['COOPERATE_COOPERATE_SCORE']

except KeyError as e:
    raise KeyError(f"Missing required environment variable: {e}")

game_description = f"""
Welcome to the Iterated Prisoner's Dilemma Game! In this game, you will make a series of decisions across multiple rounds, choosing whether to COOPERATE or DEFECT in each interaction with another player. The outcome of your decisions will affect not only your own score but also that of your opponent, based on the following payoff matrix:

COOPERATE-DEFECT: If you cooperate and your opponent defects, you will score {coop_def_score} points while your opponent scores {def_coop_score} points.
DEFECT-COOPERATE: If you defect and your opponent cooperates, you will score {def_coop_score} points while your opponent scores {coop_def_score} points.
DEFECT-DEFECT: If both you and your opponent choose to defect, each of you will score {def_def_score} points.
COOPERATE-COOPERATE: If both you and your opponent cooperate, each of you will score {coop_coop_score} points.

Your decisions and their consequences will accumulate over the rounds.

Rules of the Game:
1. Rounds: The game will consist of an undefined number of rounds.
2. Decision Making: In each round, you must choose to either "COOPERATE" or "DEFECT." You will make your choice simultaneously with your opponent, without knowledge of their decision.
3. Scoring: After each round, points will be awarded based on the choices made by you and your opponent according to the payoff matrix.
4. Strategy: You are encouraged to develop a strategy based on the outcomes of previous rounds. Pay close attention to your opponent's past behavior, as it may give you insights into their future actions.
"""