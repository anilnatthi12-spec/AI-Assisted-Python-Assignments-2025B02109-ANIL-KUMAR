# ...existing code...

# Iterative version of factorial
def factorial_iterative(n):
	"""
	Returns the factorial of n using an iterative approach.
	"""
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result

# Recursive version of factorial
def factorial_recursive(n):
	"""
	Returns the factorial of n using recursion.
	"""
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial_recursive(n - 1)
if __name__ == "__main__":
    while True:
        user_input = input("Enter a non-negative integer for factorial (or 'q' to quit): ")
        if user_input.strip().lower() == 'q':
            print("Exiting.")
            break
        try:
            n = int(user_input)
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a non-negative integer.")
            continue
        print(f"Iterative factorial of {n}: {factorial_iterative(n)}")
        print(f"Recursive factorial of {n}: {factorial_recursive(n)}")
