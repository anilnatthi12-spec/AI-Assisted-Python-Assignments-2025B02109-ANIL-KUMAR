from collections import deque

class QueueAssistant:
    def __init__(self):
        self._items = deque()

    def enqueue(self, values):
        for value in values:
            self._items.append(value)
        return list(self._items)

    def dequeue(self, count):
        removed = []
        for _ in range(count):
            if not self._items:
                break
            removed.append(self._items.popleft())
        return removed, list(self._items)

    def peek(self):
        return self._items[0] if self._items else None


def parse_numbers(raw):
    return [int(part.strip()) for part in raw.split(",") if part.strip()]


def run_tests():
    q = QueueAssistant()
    assert q.peek() is None

    q.enqueue([1, 2, 3])
    assert q.peek() == 1

    removed, state = q.dequeue(2)
    assert removed == [1, 2]
    assert state == [3]

    q.enqueue([4, 5])
    assert q.peek() == 3

    removed, state = q.dequeue(5)
    assert removed == [3, 4, 5]
    assert state == []

    print("Automated tests passed.\n")


def interactive_session():
    queue = QueueAssistant()
    menu = (
        "1. Enqueue\n"
        "2. Dequeue\n"
        "3. Peek\n"
        "4. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            raw = input("Enter numbers to enqueue (comma-separated): ").strip()
            try:
                values = parse_numbers(raw)
                new_state = queue.enqueue(values)
                print(f"Queue after enqueue: {new_state}\n")
            except ValueError:
                print("Invalid input. Please enter integers separated by commas.\n")

        elif choice == "2":
            raw = input("Enter how many numbers to dequeue (comma-separated counts or single number): ").strip()
            try:
                counts = parse_numbers(raw)
                total = sum(counts)
                removed, new_state = queue.dequeue(total)
                print(f"Dequeued values: {removed}")
                print(f"Queue after dequeue: {new_state}\n")
            except ValueError:
                print("Invalid input. Please enter integer counts.\n")

        elif choice == "3":
            front = queue.peek()
            if front is None:
                print("Queue is empty.\n")
            else:
                print(f"Front value (peek): {front}\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    run_tests()
    interactive_session()