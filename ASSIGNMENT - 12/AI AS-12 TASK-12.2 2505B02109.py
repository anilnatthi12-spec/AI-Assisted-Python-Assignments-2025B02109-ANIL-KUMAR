def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps happen in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # List is already sorted
    return arr

# Main program
if __name__ == "__main__":
    try:
        # Get input from user
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.strip().split()))

        # Sort the list
        sorted_numbers = bubble_sort(numbers)

        # Display the result
        print("Sorted list:", sorted_numbers)
    except ValueError:
        print("Please enter valid integers separated by spaces.")
