class MoreThan11Students(Exception):
    def __init__(self, message="Too many students in the group! Should not exceed 11!"):
        super().__init__(message)


class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


class Group:
    MAX_STUDENTS = 10

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise MoreThan11Students("Too many students in the group! Should not exceed 11.")
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student

    def delete_student(self, last_name):
        self.students = [student for student in self.students if student.last_name != last_name]

    def __str__(self):
        return ', '.join(str(student) for student in self.students)

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group()
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
