import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


students = load_students()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = input("Roll Number: ")
        name = input("Name: ")
        course = input("Course: ")
        marks = input("Marks: ")

        student = {
            "roll": roll,
            "name": name,
            "course": course,
            "marks": marks
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    elif choice == "2":

        if not students:
            print("No records found.")

        else:
            print()

            for student in students:
                print("----------------------------")
                print("Roll   :", student["roll"])
                print("Name   :", student["name"])
                print("Course :", student["course"])
                print("Marks  :", student["marks"])

    elif choice == "3":

        roll = input("Enter Roll Number: ")

        found = False

        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":

        roll = input("Enter Roll Number to update: ")

        for student in students:

            if student["roll"] == roll:

                student["name"] = input("New Name: ")
                student["course"] = input("New Course: ")
                student["marks"] = input("New Marks: ")

                save_students(students)

                print("Record updated.")
                break

        else:
            print("Student not found.")

    elif choice == "5":

        roll = input("Enter Roll Number to delete: ")

        for student in students:

            if student["roll"] == roll:
                students.remove(student)
                save_students(students)
                print("Student deleted.")
                break

        else:
            print("Student not found.")

    elif choice == "6":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")
