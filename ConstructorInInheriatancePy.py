"""INHERITANCE:
inheritance is a mechanism where new class accquires the propeties and behaviour of an existing class. it promote code reusability and it allows creation of heirarchical relationship
among classes."""
#sub class can access all features of superclass but super class cannot access any features of subclass.
#if you create a object for subclass. first it will try to find init of subclass. if it is not find then it will class init of super class.
"""class A:
    def __init__(self):
        print("In A init")
class B:
    def show(self):
        print("hai welcome")
a=A()


class C:
    def __init__(self):
        print("In C init")
class D:
    def __init__(self):
        print("In D init...")
c=C()  """

#i want to acces the both features. with the super() we can acess all the features of parent classs.
class A:
    def __init__(self):
        print("In A init")
class B(A):
    def __init__(self):
        super().__init__() #if you have call super then it will first call init of superclass then call init of subclass.
        print("In B init...")
    def show(self):
        print("hai welcome")
b=B()

#MRO(Method Resolution Order):
#when we have multiple inheritance it will only starts from left to right which means the moment you try init it will first find init of itself,and after it prefer left one first.
#we also use super to call all other methods as well, of super class not just a init method.
