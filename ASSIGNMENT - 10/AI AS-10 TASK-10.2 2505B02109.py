def find_common(a, b):
    return list(set(a) & set(b))

# Take input from user
a = input("Enter elements of list A separated by spaces: ").split()
b = input("Enter elements of list B separated by spaces: ").split()

# Display common elements
print("Common elements:", find_common(a, b))