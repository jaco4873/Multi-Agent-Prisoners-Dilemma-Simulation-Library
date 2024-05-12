import random


def tit_for_tat(opponent_history):
    """Replicates the opponent's last action. Cooperates on the first move."""
    return opponent_history[-1] if opponent_history else "COOPERATE"


def suspicious_tit_for_tat(opponent_history):
    """Replicates the opponent's last action. Defects on the first move."""
    return opponent_history[-1] if opponent_history else "DEFECT"


def forgiving_tit_for_tat(opponent_history, forgiveness_probability=0.05):
    """Like Tit for Tat, but occasionally forgives by cooperating even after a defection, based on a specified probability."""
    if (
        not opponent_history
        or opponent_history[-1] == "COOPERATE"
        or random.random() <= forgiveness_probability
    ):
        return "COOPERATE"
    return "DEFECT"


def defection_sensitive_tit_for_tat(opponent_history, shift_threshold=5):
    """
    Cooperates on the first move, then mirrors the opponent's last move, but switches to consistent defections
    once a threshold of opponent defections is reached.
    """
    if not opponent_history:
        return "COOPERATE"
    if opponent_history.count("DEFECT") > shift_threshold:
        return "DEFECT"
    else:
        return opponent_history[-1]


def tit_for_two_tats(opponent_history):
    """Defects only if the opponent has defected in the last two consecutive rounds."""
    return "DEFECT" if opponent_history[-2:] == ["DEFECT", "DEFECT"] else "COOPERATE"


def grim_trigger(opponent_history):
    """Cooperates until the opponent defects once, after which it always defects. (Also known is Friedman Strategy)"""
    return "DEFECT" if "DEFECT" in opponent_history else "COOPERATE"


def always_cooperate(opponent_history):
    """Always cooperates"""
    return "COOPERATE"


def adaptive_strategy(opponent_history):
    """
    Adapts its action based on the relative frequency of cooperation versus defection by the opponent to allow
    mutual cooperation while being protected from exploitation.
    """
    if not opponent_history:
        return "COOPERATE"
    cooperate_count = opponent_history.count("COOPERATE")
    defect_count = opponent_history.count("DEFECT")
    if cooperate_count + defect_count != len(opponent_history):
        raise ValueError("Adaptive Strategy not working as expected.")  # Not for prod
    if cooperate_count > defect_count:
        return "COOPERATE"
    else:
        return "DEFECT"


def soft_majority(opponent_history):
    """Cooperates if the majority of actions by the opponent were cooperative, otherwise defects."""
    return (
        "COOPERATE"
        if not opponent_history
        or opponent_history.count("COOPERATE") > len(opponent_history) / 2
        else "DEFECT"
    )


def hard_majority(opponent_history):
    """Defects initially and then follows the majority action of the opponent."""
    return (
        "DEFECT"
        if not opponent_history
        or opponent_history.count("COOPERATE") <= len(opponent_history) / 2
        else "COOPERATE"
    )


def random_strategy(_):
    """Randomly chooses between cooperating and defecting."""
    return random.choice(["COOPERATE", "DEFECT"])


def betrayal(opponent_history, betrayal_turn=5):
    """Builds trust by cooperating and then strategically defects at a specific turn."""
    return "COOPERATE" if len(opponent_history) < betrayal_turn else "DEFECT"
