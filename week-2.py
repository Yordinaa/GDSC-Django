student_db = {}
#create a database to store student records
def add_student():
    name = input("Please enter student name: ")
    age = input("please enter age: ")
    grade = input("Please enter grade: ")
    # Add student details to the database
    student_db[name] = {"age": age, "grade": grade}
    print(f"Student {name} added to the database.")
def view_student():
    name = input("Enter student name u want to see: ")
    # Check if student exists in database
    if name in student_db:
        print(f"Name: {name}")
        print(f"Age: {student_db[name]['age']}")
        print(f"Grade: {student_db[name]['grade']}")
    else:
        print("Student not found in the databse")
def list_students():
    for name, details in student_db.items():
        print(f"Name: {name}")
        print(f"Age: {details['age']}")
        print(f"Grade: {details['grade']}")
def update_student():
    name = input("Enter student name u want to update: ")
    if name in student_db:
        print("What data you want to update?")
        print("1. Age")
        print("2. Grade")
        choice = int(input())
        if choice == 1:
            new_age = input("What is the new age?  ")
            student_db[name]['age'] = new_age
            print("Age updated successfully")
        elif choice == 2:  
            new_grade = input("What is the new grade? ")
            student_db[name]['grade'] = new_grade
            print("Grade updated successfully")
        else:
            print("Student not found in the databse")

def delete_student():
    name = input("Enter name of student you want to delete: ")
    if name in student_db:
        del student_db[name]
        print("Student deleted from the db")
    else:
        print("Student not found in the db")
while True:
    print("""
WELCOME!!!
Press 1 to add Student
Press 2 to view Student
Press 3 to List Students
Press 4 to update Student
Press 5 to delete Student
Press 6 to Exit 
""")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        list_students()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
