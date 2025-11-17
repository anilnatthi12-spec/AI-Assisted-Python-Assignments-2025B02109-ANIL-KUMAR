# Function to check primality
def is_prime(number):
    """
    Check whether a given integer is prime.

    Args:
        number: An integer to check for primality.

    Returns:
        bool: True if prime, False otherwise.
    """
    # Ensure it's an integer
    if not isinstance(number, int):
        return False
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False

    # Check odd divisors up to sqrt(number)
    import math
    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
    return True
# Main program: interactive prime checker
if __name__ == "__main__":
    print("Prime Checker — enter integers to test. Type 'q' to quit.")
    while True:
        user_input = input("Enter an integer (or 'q' to quit): ")
        if user_input.strip().lower() == 'q':
            print("Exiting. Goodbye!")
            break

        # Validate and convert to integer
        try:
            # Reject floats like 3.5 explicitly
            if '.' in user_input or 'e' in user_input.lower():
                # allow inputs like '5.0' as integer if they represent an integer value
                val = float(user_input)
                if not val.is_integer():
                    print("Please enter an integer (no fractional part).")
                    continue
                number = int(val)
            else:
                number = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        # Check primality
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is NOT a prime number.")
