class MoreThan11Students(Exception):
    def __init__(self, message="Too many students in the group! Should not exceed 11!"):
        super().__init__(message)

class Group:
    MAX_STUDENTS = 10

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise MoreThan11Students("Too many students in the group! Should not exceed 11.")
        self.students.append(student)

my_group = Group()
try:
    for i in range(11):
        my_group.add_student(f"Student {i+1}")
except MoreThan11Students as e:
    print(f"Error: {e}")
