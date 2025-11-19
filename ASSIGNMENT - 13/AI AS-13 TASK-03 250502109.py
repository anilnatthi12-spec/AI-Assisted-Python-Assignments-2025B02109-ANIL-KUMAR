class Student:
    """    Represents a student with name, age, and a list of marks.
    """
    def __init__(self, name, age, marks):
        """
        Initializes a Student object.

        Parameters:
        name (str): Student's name.
        age (int): Student's age.
        marks (list of int or float): List of marks in subjects.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """Displays the student's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        """Returns the total of all marks."""
        return sum(self.marks)

# Sample usage with user input
if __name__ == "__main__":
    try:
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        marks_input = input("Enter three marks separated by spaces: ")
        marks = list(map(float, marks_input.strip().split()))

        if len(marks) != 3:
            raise ValueError("Please enter exactly three marks.")

        student = Student(name, age, marks)
        student.show_details()
        print(f"Total Marks: {student.total_marks()}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")