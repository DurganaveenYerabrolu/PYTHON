#operating overloading.
"""operating overloading in python means provide extending meaning beyond their predefined operational meaning.
the user has to add two objects using "+" operator , and it will gives an error.this is because compiler does not know how to add two objects. so the user has to define the function for
using the operator and the process is knowm as operator overloading.
python provides some special functions or we can say magic functions for performing operator overloading, which is automatically invoked when it is associated with that operator. such as
when the user uses the "+" operator, the magic function __add__ will automatically invoked in the command where "+" operator will be defined.  """
a=5
b=6
print(a+b)   #5,6 are operands and + is operator.
print(int.__add__(a,b))

st="hello"
s="world"
print(st+s)
print(str.__add__(st,s))

#whatever happens with python is with the help of objects.here a,b type of it is 'int'. int is a class here. when you say class, class has some certain methods.like __int__,__sub__,__abs__ ..

#MAGIC METHODS:
"""we have different methods for different operators.
the moment you use '+' it will call __add__ method.
__add__(), __sub__(), __mul__(),__gt__() etc.  """


"""class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

s1=Student(1,2)
s2=Student(2,35)
s3=s1+s2   """    #error
#behind the scene we call use '+' with integer. it will call add method. but our class dont have __add__() method.
"""if you need to add two Student you need to overload "+". Because integer knows what is +, string knows what is +. a Class (Student) dont known   what is + means. "+" means calling the
__add__() method here we have to define our own method. """


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __str__(self):    #override for returning the values, not object address.
        return "{} {}".format(self.m1,self.m2)

s1=Student(1,2)
s2=Student(2,35)
s3=s1+s2      #---> means Student.__add__(s1,s2)
print(s3.m1)
print(s3)     #it gives the address.we want values.
#so whenever you try to print the object doesn't matter it is integer,or your class. behind the scene it is calling a method called as __str__():
#so we want values we need to override the method.

#if you want to perform an operation on the objects which are user define, you have to define all methods(required).


class st:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

s4=st(12,35)
s5=st(34,56)
if s4>s5:
    print("s1 is max:")
else:
    print("s2 is max:")
