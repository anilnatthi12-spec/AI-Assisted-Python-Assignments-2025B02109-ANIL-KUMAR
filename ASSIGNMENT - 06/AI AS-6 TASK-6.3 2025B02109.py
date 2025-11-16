# Program to classify age groups using nested if-elif-else

def classify_age(age):
    if age >= 0:
        if age < 13:
            print("Child")
        elif age < 20:
            print("Teenager")
        elif age < 60:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Invalid age")

# Calling the function
age = int(input("Enter age: "))
classify_age(age)
