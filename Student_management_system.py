students = []

# 1. ADD STUDENT
def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks (out of 300): "))

    percentage = marks / 3

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "percentage": percentage
    }

    students.append(student)
    print("\nStudent added successfully!")


# 2. VIEW STUDENTS
def view_student():
    if len(students) == 0:
        print("\nNo student records found!")
        return

    for s in students:
        print(f"Name: {s['name']} , Roll: {s['roll']} , Marks: {s['marks']} , Percentage: {s['percentage']}")
    print()


# 3. SEARCH STUDENT
def search_student():
    roll = int(input("Enter roll number: "))

    for s in students:
        if roll == s["roll"]:
            print(f"Name: {s['name']} , Roll: {s['roll']} , Marks: {s['marks']} , Percentage: {s['percentage']}")
            return

    print("Student not found!")


# 4. UPDATE STUDENT
def update_student():
    roll = int(input("Enter roll number to update: "))

    for s in students:
        if roll == s["roll"]:
            s["name"] = input("Enter new name: ")
            s["marks"] = float(input("Enter new marks: "))
            s["percentage"] = s["marks"] / 3

            print("Student updated successfully!")
            return

    print("Student not found!")


# 5. DELETE STUDENT
def delete_student():
    roll = int(input("Enter roll number to delete: "))

    for s in students:
        if roll == s["roll"]:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# 6. MENU
def menu():
    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter choice (1-6): "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_student()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

#7. START PROGRAM
menu()