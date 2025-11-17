class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end.")

    def display(self):
        """Display the linked list."""
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        print("Linked list contents:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Demo: interactively take input from user
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\nChoose an operation:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Display list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = input("Enter data to insert at beginning: ")
            ll.insert_at_beginning(data)
        elif choice == '2':
            data = input("Enter data to insert at end: ")
            ll.insert_at_end(data)
        elif choice == '3':
            ll.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")