"""
Static methods = A method that belong to a class rather than any object from that class (instance)
                 Usually used for general utility functions

Instance methods = Best for operations on instances of the class (objects)

@instancemethod
def get_info(self) :
    return f"{self. name} = {self. position}"

Static methods = Best for utility functions that do not need access to class data

@staticmethod
def km_to_miles (kilometers) :
    return kilometers * 0.621371
""" 


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info (self) :
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashiier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Cleaner"))  # False