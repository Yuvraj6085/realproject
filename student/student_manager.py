# student_manager.py
import json
import os
from student import Student

class StudentManager:
    def __init__(self, filename="data/students.json"):
        self.filename = filename
        self.students = {}  # {student_id: Student}
        self.load_students()

    def add_student(self, student: Student):
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists.")
        self.students[student.student_id] = student
        self.save_students()
        print(f"✅ Added: {student.name}")

    def view_all_students(self):
        if not self.students:
            print("📭 No students in the system.")
            return
        print("\n" + "="*100)
        print("STUDENT LIST")
        print("="*100)
        for student in self.students.values():
            print(student)
        print("="*100)

    def find_student(self, student_id: str):
        return self.students.get(student_id.strip().upper())

    def search_students(self, query: str):
        query = query.strip().lower()
        results = [
            s for s in self.students.values()
            if query in s.name.lower() or query in s.student_id.lower() or query in s.email.lower()
        ]
        return results

    def update_student(self, student_id: str, name=None, email=None, age=None):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")

        if name is not None:
            student.name = student._validate_name(name)
        if email is not None:
            student.email = student._validate_email(email)
        if age is not None:
            student.age = student._validate_age(age)

        self.save_students()
        print(f"✅ Updated: {student.name}")

    def delete_student(self, student_id: str):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        removed = self.students.pop(student_id)
        self.save_students()
        print(f"🗑️ Deleted: {removed.name}")

    def enroll_student(self, student_id: str, course: str, grade: str):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        student.add_course(course, grade)
        self.save_students()
        print(f"✅ Enrolled {student.name} in {course} with grade {grade}.")

    def view_enrollments(self, student_id: str):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        if not student.enrollments:
            print(f"📭 {student.name} has no courses.")
        else:
            print(f"\n📚 {student.name}'s Courses:")
            for course, grade in student.enrollments.items():
                print(f"  {course}: {grade}")

    def save_students(self):
        try:
            data = {sid: s.to_dict() for sid, s in self.students.items()}
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def load_students(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for student_id, student_data in data.items():
                        self.students[student_id] = Student.from_dict(student_data)
        except Exception as e:
            print(f"⚠️  Could not load students: {e}")