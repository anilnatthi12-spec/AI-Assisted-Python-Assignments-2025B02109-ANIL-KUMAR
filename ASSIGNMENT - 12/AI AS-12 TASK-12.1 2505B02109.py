def linear_search(arr, target):
    """
    Searches for the target in the list and returns its index if found, else -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
# Main program
if __name__ == "__main__":
    try:
        # Get list input from user
        user_input = input("Enter list elements separated by spaces: ")
        arr = user_input.split()

        # Get target value to search
        target = input("Enter the value to search for: ")

        # Perform linear search
        index = linear_search(arr, target)

        # Display result
        if index != -1:
            print(f"Value '{target}' found at index {index}.")
        else:
            print(f"Value '{target}' not found in the list.")
    except Exception as e:
        print(f"An error occurred: {e}")