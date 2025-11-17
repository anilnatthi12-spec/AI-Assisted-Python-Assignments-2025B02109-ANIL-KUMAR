class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        """Remove and return the top item of the stack. Return None if stack is empty."""
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from stack.")
            return popped_item
        print("Stack is empty. Cannot pop.")
        return None

    def peek(self):
        """Return the top item of the stack without removing it. Return None if stack is empty."""
        if not self.is_empty():
            top_item = self.items[-1]
            print(f"Top item is {top_item}.")
            return top_item
        print("Stack is empty. Nothing to peek.")
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

# Demo: interactively take input from user
if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")