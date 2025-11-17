def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Take number from user
n = int(input("Enter a number: "))

# Calculate and print result
print("Sum of first", n, "numbers is:", sum_to_n(n))
