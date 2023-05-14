# TASK 2

class Student:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __repr__(self):
        return self.name


student1 = Student("an10000", "Ali")
student2 = Student("an10001", "Vali")
student3 = Student("an10002", "Salim")
student4 = Student("an10003", "Karim")
student5 = Student("an10004", "Asror")
student6 = Student("an10005", "Akrom")
students = []
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)
students.append(student6)

# 1ST WAY
# students = [students[i] for i in range(len(students)-1, -1, -1)]
# print(students)

# 2ND WAY
print(list(reversed(students)))
