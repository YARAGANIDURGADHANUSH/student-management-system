import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Course: {info['course']}")

def update_student(students):
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student not found.")
        return

    students[student_id]["name"] = input("Enter New Name: ")
    students[student_id]["age"] = input("Enter New Age: ")
    students[student_id]["course"] = input("Enter New Course: ")
    save_students(students)
    print("Student updated successfully!")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
