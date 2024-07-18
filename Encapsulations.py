#Encapsulation
"""it is the process of combining attributes(variables inside the class) and methods(functions inside class)in same class.by acess modifiers we can achieve encapsulation.
PUBLIC:Accessible and usable by anyone.both within and outside class.   a
PRIVATE:Acessible only within the class where it is defined,not accessible outside the class __a
PROTECTED:Accessible within the class and its subclasses,discourages direct acess from outside the class hierarchy. _a
Public:"""
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
a=A(1,2)
a.add()
print(a.a) #outside acess.
#private
class B:
    __a=10
    __b=34
    def display(self):#private members can only acess by the public methods of the smae class
        print(self.__a+self.__b)
b1=B()
b1.display()
#print(b1.__a) cannot acess outside the class
#protected
class C:
    _c=34
class D(C):
    def show(self):
        print(self._c)
d=D()
d.show()
