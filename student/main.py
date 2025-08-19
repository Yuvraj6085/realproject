# main.py
from student_manager import StudentManager

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid integer.")

def main():
    manager = StudentManager()

    while True:
        print("\n🎓 STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Enroll in Course")
        print("7. View Student Courses")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == '1':
            print("\n📝 ADD NEW STUDENT")
            student_id = input("Student ID (e.g., CS1001): ").strip()
            name = input("Full Name: ").strip()
            email = input("Email: ").strip()
            age = get_int_input("Age: ")

            try:
                manager.add_student(Student(student_id, name, email, age))
            except ValueError as e:
                print(f"❌ Failed to add student: {e}")

        elif choice == '2':
            manager.view_all_students()

        elif choice == '3':
            query = input("Search by name, ID, or email: ").strip()
            results = manager.search_students(query)
            if results:
                print(f"\n🔍 Found {len(results)} result(s):")
                for s in results:
                    print(s)
            else:
                print("📭 No matching students found.")

        elif choice == '4':
            student_id = input("Enter student ID to update: ").strip()
            student = manager.find_student(student_id)
            if not student:
                print("❌ Student not found.")
            else:
                print(f"Current: {student}")
                print("Leave blank to keep unchanged.")
                name = input("New name: ").strip() or None
                email = input("New email: ").strip() or None
                age_input = input("New age: ").strip()
                age = int(age_input) if age_input.isdigit() else None

                try:
                    manager.update_student(student_id, name, email, age)
                except ValueError as e:
                    print(f"❌ {e}")

        elif choice == '5':
            student_id = input("Enter student ID to delete: ").strip()
            try:
                manager.delete_student(student_id)
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == '6':
            student_id = input("Student ID: ").strip()
            course = input("Course name: ").strip()
            grade = input("Grade (A/B/C/D/F): ").strip().upper()
            try:
                manager.enroll_student(student_id, course, grade)
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == '7':
            student_id = input("Student ID: ").strip()
            try:
                manager.view_enrollments(student_id)
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == '8':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1–8.")

if __name__ == "__main__":
    main()