def check_even_odd(number):
    """
    Function to check whether a given number is even or odd
    
    Args:
        number: An integer to check
    
    Returns:
        str: A string indicating whether the number is even or odd
    """
    if isinstance(number, (int, float)):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Please enter a valid number"


# Function to reverse a string
def reverse_string(s):
    """
    Returns the reverse of the input string s.
    """
    return s[::-1]


if __name__ == "__main__":
    # Interactive string reversal
    user_str = input("Enter a string to reverse: ")
    reversed_str = reverse_string(user_str)
    print(f"Reversed string: {reversed_str}")
