def sum_of_squares_from_input() -> int:
    """
    Prompt the user to enter integers and return the sum of their squares.

    The function accepts input in flexible formats, e.g.:
    - Space separated: 1 2 3
    - Comma separated: 1,2,3
    - Mixed separators: 1, 2  3,4

    Returns:
        int: The sum of squares of all parsed integers.
    """
    raw = input("Enter integers (separated by space or comma): ").strip()
    if not raw:
        print("No input provided. Sum = 0")
        return 0

    # Normalize separators to spaces, then split
    normalized = raw.replace(",", " ")
    tokens = [t for t in normalized.split() if t]

    numbers = []
    for token in tokens:
        try:
            numbers.append(int(token))
        except ValueError:
            raise ValueError(f"Invalid integer: '{token}'")

    result = sum(n * n for n in numbers)
    print(f"Sum of squares: {result}")
    return result


def main():
    """Interactive runner for sum_of_squares_from_input()."""
    try:
        sum_of_squares_from_input()
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
    