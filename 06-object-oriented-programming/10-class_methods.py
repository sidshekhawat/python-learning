"""
Class methods = Allow operations related to the class itself
                Take (cls) as the first parameter, which represents the class itself.
"""

"""
Instance methods = Best for operations on instances of the class (objects)
Static methods = Best for utility functions that do not need access to class data
Class methods = Best for class-level data or require access to the class itself
"""

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa  = gpa    
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count :.2f}"

student1 = Student("John", 2.5)
student2 = Student("Jane", 3.8)
student3 = Student("Mike", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())