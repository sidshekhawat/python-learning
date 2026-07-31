"""
Polymorphism = Greek word that means to "have many forms or faces"
               Poly = Many
               Morphe = Form

               TWO WAYS TO ACHIEVE POLYMORPHISM
                1. Inheritance = An object could be treated of the same type as a parent class
                2. "Duck typing" = Object must have necessary attributes/methods


"Duck typing" = Another way to achieve polymorphism besides Inheritance
                Object must have the minimum necessary attributes/methods
                "If it looks like a duck and quacks like a duck, it must be a duck."

"""


class Animal:
    alive = True

class Dog(Animal):
    def speak (self) :
        print ("WOOF!")

class Cat (Animal):
    def speak (self) :
        print ("MEOW!")

class Car:

    alive = True
    
    def speak (self):
        print("HONK!")

animals = [Dog(), Cat (),Car () ]

for animal in animals:
    animal. speak()
    print (animal. alive)