try:
    user_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, user_input.strip().split()))
    squares = [i * i for i in nums]
    print("Squares:", squares)
except ValueError:
    print("Please enter valid integers separated by spaces.")