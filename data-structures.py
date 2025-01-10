# Student Data Management System
students = {}  # Dictionary to store student data

def create_student():
    """Create a new student entry."""
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists.")
        return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grades = input("Enter Grades: ").split(",")
    students[student_id] = {
        "name": name,
        "age": age,
        "grades": [grade.strip() for grade in grades]
    }
    print("Student added successfully!")

def retrieve_student():
    """Retrieve a student's information."""
    student_id = input("Enter Student ID to retrieve: ")
    if student_id in students:
        student = students[student_id]
        print(f"ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {', '.join(student['grades'])}")
    else:
        print("Student ID not found.")

def update_student():
    """Update an existing student's information."""
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        print("Leave field blank to keep current value.")
        name = input(f"Enter new Name (current: {students[student_id]['name']}): ")
        age = input(f"Enter new Age (current: {students[student_id]['age']}): ")
        grades = input(f"Enter new Grades (current: {', '.join(students[student_id]['grades'])}): ")

        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = int(age)
        if grades:
            students[student_id]['grades'] = [grade.strip() for grade in grades.split(",")]

        print("Student updated successfully!")
    else:
        print("Student ID not found.")

def delete_student():
    """Delete a student's information."""
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")

def display_all_students():
    """Display all students."""
    if not students:
        print("No students found.")
    else:
        for student_id, student in students.items():
            print(f"ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grades: {', '.join(student['grades'])}")

def main():
    """Main menu for the student management system."""
    while True:
        print("\n--- Student Data Management ---")
        print("1. Create Student")
        print("2. Retrieve Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_student()
        elif choice == '2':
            retrieve_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
