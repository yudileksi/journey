# Class Variables
#       = shared among all instances of a class
#       = Defined outside the constructor ("def" functions)
#       = Allow you to share data to all objects created from that class
from idlelib.pyparse import trans
from symtable import Class

#class Student:                                  # CLASS

#    class_year = 2022                           # CLASS VARIABLES
#    num_students = 0                            # Defined outside constructor and Shared among all objects (self)

#    def __init__(self, name, age):              # CONSTRUCTOR
#        self.name = name
#        self.age = age
#        Student.num_students += 1

#student1 = Student("Spongebob", 15)
#student2 = Student("Patrick", 16)
#student3 = Student("Squidward", 21)
#student4 = Student("Sandy", 19)

#print(f"Graduation class of {Student.class_year} has {Student.num_students} students :")
#print(student1.name)
#print(student2.name)
#print(student3.name)
#print(student4.name)


# -------------------------------------------------------------------------------------------- #
# INHERITANCES (Children classes)
#       - Allows class to inherit attributes and methods from another class
#       - Helps code with reusability & extensibility
#       - Class child (parent)

#class Animal:
#    def __init__(self, name):           # Why no is_alive inside parenthesis?
#        self.name = name
#        self.is_alive = True

#    def eat(self):
#        print(f"{self.name} is eating")

#    def sleep(self):
#        print(f"{self.name} is sleeping")

#class Dog(Animal):
#    def speak(self):
#        print("WOOF!")

#class Cat(Animal):
#    def speak(self):
#        print("MEOW")

#class Mouse(Animal):
#    def speak(self):
#        print("SQUICK!")

#dog = Dog("Scooby")
#cat = Cat("Tom")
#mouse = Mouse("Jerry")

#print(mouse.name)
#print(mouse.is_alive)
#mouse.eat()
#mouse.sleep()
#ouse.speak()

# -------------------------------------------------------------------------------------------- #
# super()
#       - function used in child class to call methods from a parent class
#       - allow to extend the functionality of the inherited methods
#       - to reuse the constructor of a parent class

#class Shape:
#    def __init__(self, color, is_filled):
#        self.color = color
#        self.is_filled = is_filled

#    def describe(self):
#        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

#class Circle(Shape) :
#    def __init__(self, color, is_filled, radius):
#        super().__init__(color, is_filled)
#        self.radius = radius

#    def describe(self):
#        print(f"It is circle with area of {3.14 * self.radius ** 2} cm^2")
#        super().describe()

#class Square(Shape):
#    def __init__(self, color, is_filled, width):
#        super().__init__(color, is_filled)
#        self.width = width

#    def describe(self):
#            print(f"It is square with area of {self.width ** 2} cm^2")
#            super().describe()

#class Triangle(Shape):
#    def __init__(self, color, is_filled, width, height):
#        super().__init__(color, is_filled)
#        self.width = width
#        self.height = height

#    def describe(self):
#            print(f"It is triangle with area of {self.width * self.height / 2} cm^2")
#            super().describe()

#circle = Circle("red", True, 5)
#square = Square("blue", False, 10)
#triangle = Triangle("yellow", True, 7, 5)

#circle.describe()
#print()
#square.describe()
#print()
#triangle.describe()


# -------------------------------------------------------------------------------------------- #
# POLYMORPHISM
#       - Greek word that means to "Have many forms or faces
#           Poly = Many
#           morphe = Form

from abc import ABC, abstractmethod         # used to force subclass to implement something defined in the parent

class Shape:

    @abstractmethod                         # used to force subclass to implement something defined in the parent
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Pizza(Circle):                                # This class(pizza) is other form of shape but can use the circle of
    def __init__(self, topping, radius):            # construction that has parent of shape
        self.topping = topping                      # that's the polymorphism (many form)
        super().__init__(radius)

shapes = [Circle(5), Square(6), Triangle(5, 6), Pizza("cheese", 6)]

for shape in shapes:
    print(shape.area())