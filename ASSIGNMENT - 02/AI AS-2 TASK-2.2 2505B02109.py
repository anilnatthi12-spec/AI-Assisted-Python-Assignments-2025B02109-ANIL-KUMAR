def is_palindrome(number: int) -> bool:
    """
    Check if a given number is a palindrome.
    
    A number is a palindrome if it reads the same forwards and backwards.
    For example: 121, 1221, 12321 are palindromes.
    
    Args:
        number: The integer to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert number to string for easier comparison
    num_str = str(abs(number))  # Handle negative numbers by taking absolute value
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]


def main():
    """Interactive prompt to check if a number is a palindrome."""
    print("Palindrome Number Checker")
    print("-" * 22)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a number to check (or 'q' to quit): ")
            
            # Check for quit condition
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
            
            # Convert input to integer and check if it's a palindrome
            number = int(user_input)
            result = is_palindrome(number)
            
            # Print result with explanation
            if result:
                print(f"✓ {number} is a palindrome!")
                print(f"  It reads the same forwards and backwards: {abs(number)}")
            else:
                print(f"✗ {number} is not a palindrome.")
                print(f"  Forwards: {abs(number)}")
                print(f"  Backwards: {str(abs(number))[::-1]}")
                
        except ValueError:
            print("Please enter a valid integer number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == '__main__':
    main()
