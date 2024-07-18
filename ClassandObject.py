#OOPS
"""oop is a way of writing the computer programs where you organize your code around the idea of objects.these objects are like building blocks that contain both data(attributes) and functions(like actions).
oop help make your code more organized,reusable,and easier to understand.
main topics in oop
1.class and objects
2.Encapsulation
3.Inheritance
4.Abstraction
5.polymorphism
1.classes and objects:
class:class is like a blueprint that defines properties and behavior that object of a certain type will have.it a template for creating objects with similar characteristics and functionalities.
object:an object is a fundamental unit of oop that combines both data(attributes) and functionality(methods).it represents a real world entity or concept and can interact with other objects.
In simpler terms an object is like a thing or an entity that has both properties and actions."""
class Student:
    def __init__(self,name,age,rollno):
        self.name=name;
        self.age=age;
        self.rollno=rollno;
    def get(self):
        print(self.name,self.age)

obj=Student("dn",23,"20fjd")
obj.get()

#example
class Bookstore:
    
