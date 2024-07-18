#METHOD OVERLOADING.
"""method overloading in python is not supported. this is an example of compile time polymorphism.
methods with the same name with different types of arguments, different number of parameters or both. these methods are called overloaded methods and this is called method overloading.
The problem with method overloading in python is that we may overload the methods but can only use the latest defined method."""
class st:
    def sum(self,a,b,c):
        s=a+b
        return s
    """def sum(self,a,b):
        si=a+b
        return si"""
s1=st()
print(s1.sum(2,34,5))
#print(s1.sum(2,3))



class student:
    def sum1(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
stt=student()
print(stt.sum1(1,24))
print(stt.sum1(1,3,4))


#METHOD OVERRIDING:
"""this is an example of runtime polymorphism. In the concept of inheritance, both classes have the same method name & same parameter.
in this, the specific implementation of the method that is already provided by the parent class is provided by the child class.it is used to change the behaviour of existing methods and
there is a need for at least two classes for method overriding. inheritance always required as it is done between parent class and child class methods. """
class A:
    def show(self):
        print("in A show...")
class B(A):
    def show(self):
        print("In B show...")     #new class overrides the properties of child class.
b=B()
b.show()
