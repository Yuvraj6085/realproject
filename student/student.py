# student.py
import re
from datetime import datetime

class Student:
    def __init__(self, student_id: str, name: str, email: str, age: int):
        self.student_id = self._validate_id(student_id)
        self.name = self._validate_name(name)
        self.email = self._validate_email(email)
        self.age = self._validate_age(age)
        self.enrollments = {}  # {course: grade}
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _validate_id(self, student_id: str) -> str:
        if not student_id or not re.match(r"^[A-Z]{2}\d{4}$", student_id.strip().upper()):
            raise ValueError("ID must be like: CS1001")
        return student_id.strip().upper()

    def _validate_name(self, name: str) -> str:
        name = name.strip()
        if not name or not re.match(r"^[A-Za-z\s]{2,50}$", name):
            raise ValueError("Name must be 2–50 letters.")
        return name.title()

    def _validate_email(self, email: str) -> str:
        email = email.strip().lower()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        return email

    def _validate_age(self, age: int) -> int:
        if not isinstance(age, int) or age < 5 or age > 150:
            raise ValueError("Age must be between 5 and 150.")
        return age

    def add_course(self, course: str, grade: str):
        course = course.strip().title()
        grade = grade.upper().strip()
        if not course:
            raise ValueError("Course name cannot be empty.")
        if grade not in ["A", "B", "C", "D", "F"]:
            raise ValueError("Grade must be A, B, C, D, or F.")
        self.enrollments[course] = grade

    def update_course_grade(self, course: str, new_grade: str):
        course = course.strip().title()
        if course not in self.enrollments:
            raise ValueError(f"Not enrolled in {course}.")
        self.add_course(course, new_grade)  # Reuse validation

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "enrollments": self.enrollments,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            student_id=data["student_id"],
            name=data["name"],
            email=data["email"],
            age=data["age"]
        )
        student.enrollments = data.get("enrollments", {})
        student.created_at = data.get("created_at", "Unknown")
        return student

    def __str__(self):
        courses = ", ".join([f"{c}({g})" for c, g in self.enrollments.items()]) or "None"
        return (f"ID: {self.student_id} | Name: {self.name} | "
                f"Age: {self.age} | Email: {self.email} | "
                f"Courses: {courses}")