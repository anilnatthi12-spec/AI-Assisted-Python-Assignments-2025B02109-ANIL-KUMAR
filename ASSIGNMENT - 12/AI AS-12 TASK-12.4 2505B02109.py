def f(x):
    return 2 * x**3 + 4 * x + 5

def df(x):
    # Derivative of f(x): f'(x) = 6x^2 + 4
    return 6 * x**2 + 4

def gradient_descent(x0, learning_rate, iterations):
    x = x0
    for i in range(iterations):
        grad = df(x)
        x = x - learning_rate * grad
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}")
    return x

# Main program
if __name__ == "__main__":
    try:
        x0 = float(input("Enter initial guess for x: "))
        learning_rate = float(input("Enter learning rate (e.g., 0.01): "))
        iterations = int(input("Enter number of iterations: "))

        result = gradient_descent(x0, learning_rate, iterations)
        print(f"\nEstimated minimum at x = {result:.6f}, f(x) = {f(result):.6f}")
    except Exception as e:
        print(f"Error: {e}")