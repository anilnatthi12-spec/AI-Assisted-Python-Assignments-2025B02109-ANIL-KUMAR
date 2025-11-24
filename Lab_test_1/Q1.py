
def fibonacci_sequence():
    try:
        n = int(input("Enter the value: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    fib_series = []
    a, b = 0, 1
    count = 0

    while count < n:
        fib_series.append(a)
        a, b = b, a + b
        count += 1

    print("Fibonacci series:")
    print(' '.join(str(num) for num in fib_series))

fibonacci_sequence()
