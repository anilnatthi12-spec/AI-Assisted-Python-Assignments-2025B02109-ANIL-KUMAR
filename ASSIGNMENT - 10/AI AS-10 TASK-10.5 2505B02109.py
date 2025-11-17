def divide_numbers(a, b):
    """
    Divides two numbers and handles division by zero.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of division if valid.
        str: Error message if division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Take input from user
try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    result = divide_numbers(a, b)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")