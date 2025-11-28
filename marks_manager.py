# Student Marks Management System
# File name: marks_manager.py

# Each student: { "roll": "1", "name": "Rohini", "marks": [80, 90, 85], "total": 255, "percentage": 85.0, "grade": "A" }

students = []  # list to store all students


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    # grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"
    return total, percentage, grade


def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")

    print("Enter marks for 3 subjects:")
    m1 = int(input("Subject 1 marks: "))
    m2 = int(input("Subject 2 marks: "))
    m3 = int(input("Subject 3 marks: "))

    marks = [m1, m2, m3]
    total, percentage, grade = calculate_result(marks)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print(f"\nStudent {name} added successfully!\n")


def display_all_students():
    print("\n--- All Students ---")
    if not students:
        print("No students found.\n")
        return

    for s in students:
        print(f"Roll: {s['roll']}")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Percentage: {s['percentage']:.2f}")
        print(f"Grade: {s['grade']}")
        print("-" * 25)
    print()


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found:")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Total: {s['total']}")
            print(f"Percentage: {s['percentage']:.2f}")
            print(f"Grade: {s['grade']}\n")
            return

    print("Student not found.\n")


def main_menu():
    while True:
        print("===== Student Marks Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, please try again.\n")


# Program start
if __name__ == "__main__":
    main_menu()
