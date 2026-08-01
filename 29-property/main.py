"""
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
            Benefit: Add additional logic when read, write, or delete attributes
            Gives you getter, setter, and deleter method
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height


    @property      #Will be called when the width attribute is accessed
    def width(self):
        return f"{self._width: .1f}cm"

    @width.setter  #Will be called when the width attribute is set to a new value
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be a positive number")

    @width.deleter #Will be called when the width attribute is deleted using the del statement
    def width(self):
        print("Deleting width...")
        del self._width
        print("Width deleted successfully.")


    @property      #Will be called when the height attribute is accessed
    def height(self):
        return f"{self._height: .1f}cm"

    @height.setter #Will be called when the height attribute is set to a new value
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Height must be a positive number")

    @height.deleter #Will be called when the height attribute is deleted using the del statement
    def height(self):             
        print("Deleting height...")
        del self._height
        print("Height deleted successfully.")

        
    @property #Will be called when the area attribute is accessed
    def area(self):
        return self.width * self.height

    @property #Will be called when the perimeter attribute is accessed
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property #Will be called when the diagonal attribute is accessed
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

rectangle = Rectangle(5, 10)

rectangle.width = 7    # Will call the setter method for width
rectangle.height = 12  #  #Will call the setter method for height


print("Rectangle properties:")        #Will call the getter method for width and height
print(f"Width: {rectangle.width}")    #Will call the getter method for width
print(f"Height: {rectangle.height}")  #Will call the getter method for height
#print(f"Area: {rectangle.area}")     #Will call the getter method for area
#print(f"Perimeter: {rectangle.perimeter}")   #Will call the getter method for perimeter
#print(f"Diagonal: {rectangle.diagonal}")     #Will call the getter method for diagonal

del rectangle.width  #Will call the deleter method for width
del rectangle.height #Will call the deleter method for height
