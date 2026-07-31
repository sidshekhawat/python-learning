"""
multiple inheritance = inherit from more than one parent class
                       C(A, B)
"""
"""
multilevel inheritance = inherit from a parent which inherits from another parent
                        C(B) <- B(A) <- A
"""

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep (self):
        print(f"{self.name} is sleeping")

class Prey(Animal):           #Parent class     Mulitlevel Inheritance    Inheriting from other parent class i.e. class Animal
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):       #Parent class     Mulitlevel Inheritance    Inheriting from other parent class i.e. class Animal
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):    #Children class
    pass

class Hawk(Predator):  #Children class
    pass

class Fish(Prey, Predator):      #Children class     Multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.sleep()