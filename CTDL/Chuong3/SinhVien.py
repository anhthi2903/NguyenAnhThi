class Student:
    def __init__(self, id, name, class_name, mark1, mark2):
        self.id = id
        self.name = name
        self.class_name = class_name
        self.mark1 = mark1
        self.mark2 = mark2
        self.average = (mark1 + mark2) / 2
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 9:
            return "Xuất sắc"
        elif self.average >= 8:
            return "Giỏi"
        elif self.average >= 6.5:
            return "Khá"
        elif self.average >= 5:
            return "Trung Bình"
        else:
            return "Yếu"

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    def update_student(self, student_id, new_data):
        for student in self.students:
            if student.id == student_id:
                for key, value in new_data.items():
                    setattr(student, key, value)

    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, Class: {student.class_name}, Average: {student.average}, Grade: {student.grade}")

    def calculate_average_mark1(self):
        total_mark1 = sum(student.mark1 for student in self.students)
        return total_mark1 / len(self.students)

    def calculate_average_mark2(self):
        total_mark2 = sum(student.mark2 for student in self.students)
        return total_mark2 / len(self.students)

    def find_lowest_average_student(self):
        lowest_student = min(self.students, key=lambda student: student.average)
        return lowest_student

    def find_highest_average_student(self):
        highest_student = max(self.students, key=lambda student: student.average)
        return highest_student

    def sort_students_by_class_and_average(self):
        self.students.sort(key=lambda student: (student.class_name, -student.average))

# Khởi tạo đối tượng School
school = School()

# Thêm sinh viên
student1 = Student(1, "Alice", "Class A", 8.5, 9.0)
student2 = Student(2, "Bob", "Class B", 7.0, 8.0)
school.add_student(student1)
school.add_student(student2)

# Xem danh sách sinh viên
print("Danh sách sinh viên:")
school.list_students()

# Tính điểm trung bình cho môn 1 và môn 2 của toàn bộ sinh viên
print("Điểm trung bình môn 1:", school.calculate_average_mark1())
print("Điểm trung bình môn 2:", school.calculate_average_mark2())

# Tìm sinh viên có điểm trung bình thấp nhất và cao nhất
lowest_student = school.find_lowest_average_student()
highest_student = school.find_highest_average_student()
print("Sinh viên có điểm trung bình thấp nhất:")
print(f"ID: {lowest_student.id}, Name: {lowest_student.name}, Average: {lowest_student.average}, Grade: {lowest_student.grade}")
print("Sinh viên có điểm trung bình cao nhất:")
print(f"ID: {highest_student.id}, Name: {highest_student.name}, Average: {highest_student.average}, Grade: {highest_student.grade}")

# Sắp xếp danh sách sinh viên theo lớp và điểm trung bình
school.sort_students_by_class_and_average()
print("Danh sách sinh viên sau khi sắp xếp:")
school.list_students()
