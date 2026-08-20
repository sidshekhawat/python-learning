"""
class variables = Shared among all instances of a class
                  Defined outside the constructor
                  Allow you to share data among all objects created from that class

"""

class Student:

    class_year = 2028
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student. num_students += 1

student1 = Student("Sid", 20)
student2 = Student("Veer", 20)
student3 = Student("Har", 19)
student4 = Student("Sam", 20)


#print(student1.name)
#print(student1.age)
#print(student1.class_year)     # studentt is the instance of the class
#print(Student.class_year)      # accessing class variable by class name itself

#print (Student. num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)