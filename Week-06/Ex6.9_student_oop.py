class Student:
    school = "YearUp Academy"

    def __init__(self, name, grade, track):
        self.name = name,
        self._grade = grade,
        self.track = track

    def get_grade(self):
        return self._grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self._grade = new_grade
        else:
            print("Invalid! Must be 0–100")

    def display_info(self):
        print(f"""
        ===== YearUp Academy — Student Report =====
        School : {Student.school}
        Name : {self.name}
        Grade : {self.get_grade()}
        Track : {self.track}
        """)

student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")

print(student1.get_grade())
print(student2.get_grade())

student1.set_grade(98)
student2.set_grade(150)

student1.display_info()
student2.display_info()


