class Student:
    def __init__(self, student_id: str, name: str, grade: float):
        self.id = student_id
        self.name = name
        self.grade = grade

    def __str__(self) -> str:
        grade_str = str(int(self.grade)) if self.grade.is_integer() else str(self.grade)
        return f"ID: {self.id} | Name: {self.name} | Grade: {grade_str}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id: str, name: str, grade: float) -> bool:
        if self.find_student(student_id) is not None:
            return False
        self.students.append(Student(student_id, name, grade))
        return True

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("--- Student List ---")
        for s in self.students:
            print(s)

    def find_student(self, student_id: str):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def update_grade(self, student_id: str, new_grade: float) -> bool:
        student = self.find_student(student_id)
        if student is None:
            return False
        student.grade = new_grade
        return True


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def read_grade(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            grade = float(raw)
            return grade
        except ValueError:
            print("Invalid grade. Please enter a number (e.g., 85 or 90.5).")


def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grade")
        print("4. Exit")

        choice = input("Type a number (1–4) and press Enter: ").strip()

        if choice == "1":
            student_id = read_non_empty("Enter Student ID: ")
            name = read_non_empty("Enter Name: ")
            grade = read_grade("Enter Grade: ")

            if manager.add_student(student_id, name, grade):
                print("Student added.")
            else:
                print("A student with this ID already exists.")

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = read_non_empty("Enter ID: ")
            new_grade = read_grade("Enter new grade: ")

            if manager.update_grade(student_id, new_grade):
                print("Grade updated.")
            else:
                print("Student not found.")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid option. Please choose 1–4.")


if __name__ == "__main__":
    main()