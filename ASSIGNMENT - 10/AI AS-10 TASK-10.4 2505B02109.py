def calculate_average(scores):
    return sum(scores) / len(scores)

def find_highest(scores):
    return max(scores)

def find_lowest(scores):
    return min(scores)

def process_scores(scores):
    average = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

# Take input from user
try:
    input_scores = input("Enter scores separated by commas: ")
    scores = [float(s.strip()) for s in input_scores.split(",")]
    process_scores(scores)
except ValueError:
    print("Invalid input. Please enter numeric scores separated by commas.")