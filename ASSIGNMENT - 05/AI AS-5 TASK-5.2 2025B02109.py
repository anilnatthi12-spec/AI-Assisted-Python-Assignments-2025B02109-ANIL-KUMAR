"""
File: fibonacci.py
Description: Contains a function to calculate the nth Fibonacci number 
using a recursive approach, ensuring high code transparency through detailed comments.
"""

def calculate_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using recursion.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, 8, ...).

    WARNING: This pure recursive implementation is highly inefficient due to 
    repeated calculations (O(2^n) time complexity). For practical use, 
    iterative or memoized approaches are preferred.

    Args:
        n (int): The position in the Fibonacci sequence (n >= 0).

    Returns:
        int: The nth Fibonacci number.
    """
    
    # -----------------------------------------------------------
    # 1. Base Cases (The Termination Conditions)
    # -----------------------------------------------------------
    # The recursion must stop at the first two known values of the sequence.
    
    if n < 0:
        # Handle invalid input gracefully.
        raise ValueError("Fibonacci number is not defined for negative indices.")
    
    if n == 0:
        # The 0th Fibonacci number is 0. This is the first base case.
        return 0
    
    if n == 1:
        # The 1st Fibonacci number is 1. This is the second base case.
        return 1
    
    # -----------------------------------------------------------
    # 2. Recursive Step (The Self-Call)
    # -----------------------------------------------------------
    # This is the defining part of the function, calling itself to break 
    # the problem down into smaller, identical subproblems.
    
    # The nth Fibonacci number is defined as the sum of (n-1) and (n-2) Fibonacci numbers.
    # The function effectively branches into two new calls for every step.
    
    # Recursively calculate the (n-1)th number.
    fib_n_minus_1 = calculate_fibonacci(n - 1)
    
    # Recursively calculate the (n-2)th number.
    fib_n_minus_2 = calculate_fibonacci(n - 2)
    
    # Return the sum of the two preceding numbers.
    return fib_n_minus_1 + fib_n_minus_2


# Example Usage (Demonstrating Transparency)
if __name__ == "__main__":
    test_n = 10
    
    try:
        result = calculate_fibonacci(test_n)
        print(f"Calculating the {test_n}th Fibonacci number...")
        print(f"Result (F({test_n})): {result}")
        # The 10th number should be 55 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

        test_n_error = -1
        calculate_fibonacci(test_n_error)

    except ValueError as e:
        print(f"\nCaught Expected Error: {e}")