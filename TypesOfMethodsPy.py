"""methods are classified into 3 types.
1.instance methods.
2.class methods.
3.static methods.
1.Instance methods : instance methods are the methods that are defined inside the class and are bound to an instance of the class. they are used to perform operations on the
data(attributes) of the instance
when you pass self as argument in the method then it is called instance methods. after the self the variables are called instance variables.
we are passing self it means it belongs to a particular object. it work with objects.
again itself is classified into 2 types:1.accesor methods. 2.mutator methods.
1.accessor methods:only fetch the value of an instance.getters.get the value
2.mutators:if you want to modify the value are called mutators.(set).
"""
class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1           #i want pass the values from the user.
        self.m2=m2          #pass values when you create the object.
        self.m3=m3

    def get_m(self):    #accesors(it will not changes the values. only fetch the values)
        return self.m1+self.m2+self.m3
    def set_m(self,value):     #mutators. changes the value.
        self.m1=value
s1=Student(12,4,2)
s2=Student(2,35,67)
s1.set_m(45)
res1=s1.get_m()
res2=s2.get_m()
print(res1)
print(res2)
print(s1.m1)
    
#2.class methods.
"""class variables are work with class methods.
if you work with instance you use self.
if you work with class variable you use a cls keyword.
if you want to use method as a class method then we use decorator.@classmethod."""
class Stu:
    school="Abs"
    @classmethod
    def info(cls):
        return cls.school
print(Stu.info())

#3.static method.
"""A method nothing do with instance,which has nothing do with class variable then go static method."""
def fun():
    print("hai static method.")
fun()

class stat:
    @staticmethod
    def fun1():
        print("static method...")
stat.fun1()   #we dont pass anything,not even clss or not even method.

#instance methods are work with instance variables.
#class methods are work with class variables. (one value changes will effect all objects they shared.)
#nothing to do with instance or nothing do with class then static method is used.
