class Student:
    def __init__(self, name, roll_no, grade):
        """
        Constructor to initialize student details.
        """
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_details(self):
        """
        Displays the details of the student.
        """
        print("----- Student Details -----")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Grade    : {self.grade}")
        print("----------------------------")


# Example Usage
if __name__ == "__main__":
    # Taking input from user (optional)
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    grade = input("Enter grade: ")

    student1 = Student(name, roll_no, grade)
    student1.display_details()
