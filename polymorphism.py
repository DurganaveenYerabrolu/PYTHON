#polymorphism
"""
different things can do similar in their own unique ways.
2 types:
1.compile time:Method overloading
2.runtime:method overriding
1.Method overloading:
means multiple functions or methods with the same name but different parameter.
2.method overriding:
when a subclass is redefine a method from its superclass with its own implementation.
"""
class Math:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c=0):
        print(a+b+c)

m=Math()
m.add(2,3)

class A:
    def sound(self):
        print("bark")

class B(A):
    def sound(self):
        print("meow meow:")
        #super().sound()
b=B()
b.sound()
