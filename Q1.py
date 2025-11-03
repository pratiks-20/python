
students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"Student {name} with grade {grade} added successfully.")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"Grade for {name} updated to {new_grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"Student {name} removed successfully.")
    else:
        print(f"Student {name} not found.")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade of the class: {avg:.2f}")
    else:
        print("No grades available.")

def display_extremes():
    if grades:
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")
    else:
        print("No grades available.")

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Average Grade")
    print("5. Highest & Lowest Grade")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student name to update: ")
        grade = float(input("Enter new grade: "))
        update_grade(name, grade)
    elif choice == '3':
        name = input("Enter student name to remove: ")
        remove_student(name)
    elif choice == '4':
        average_grade()
    elif choice == '5':
        display_extremes()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")