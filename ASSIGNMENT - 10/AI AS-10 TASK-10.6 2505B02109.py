def grade(score):
    """
    Returns a letter grade based on the numeric score.

    Args:
        score (float): The score to evaluate.

    Returns:
        str: Letter grade (A, B, C, D, F).
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Take input from user
try:
    score_input = float(input("Enter the score (0–100): "))
    if 0 <= score_input <= 100:
        print("Grade:", grade(score_input))
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric score.")