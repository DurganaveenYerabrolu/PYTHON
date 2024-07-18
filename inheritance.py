#inheritance
"""inheritance is a way for a class to aquire methods and attributes from another class, enabling code reuse and establishing hierarchail relations among class.
1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hierachical inheritance
5.hyprid inheritance
1.single inheritance:
a subclass inherits from only one superclass.this is the simplest of inheritance."""
class Dad:
    def dad_ph(self):
        print("this is dad phone:")
class son(Dad):
    def son_ph(self):
        print("this is son phone:")
s=son()
s.dad_ph()
s.son_ph()
"""
2.Multilevel inheritance:
a subclass inherits from subclass and another subclass inherits from the first subclass,forming a chain of inheritance."""
print("multilevel")
class grandfather:
    def gf_oh(self):
        print("this is gf phone:")
class father(grandfather):
    def f_ph(self):
        print("this is father phone:")
    
class son(father):
    def son_ph(self):
        print("this is son phone:")
s1=son()
s1.son_ph()
s1.f_ph()
s1.gf_oh()
"""
3.multiple.
a class inherits from more than one superclass.this allows the subclass to inherit attributes and methods from multiple parent classes."""
class A1:
    a=20
class B1:
    b=20
class C(A1,B1):
    def display(self):
      print(self.a+self.b)
c=C()
c.display()


class A:
    a=10

print(A.a)
"""
4.heirachical inheritance:
it involves single super Class being inherited by multiple aubclasses.each subclass can have its own behaviour in addition to the common behavoiur inherited from the super class.
opposite to multiple."""
class Aa:
    a=10
    b=20

class Bb(Aa):
    c=3
    def display(self):
        print(self.a+self.b+self.c)
class Cc(Aa):
    def show(self):
        print(self.a)
b=Bb()
b.display()
c1=Cc()
c1.show()
"""
5.Hybrid inheritance:
this involes a multiple and heirachical inheritance"""


class Umbrella:
    def __init__(self,color,price):
        self.color=color
        self.price=price
class Rain(Umbrella):
    def __init__(self,temp,fall):
        self.temp=temp
        self.fall=fall
class wind(Umbrella):
    def __init__(self,speed,color,price):
        super().__init__(color,price)
        self.speed=speed
    def display(self):
        print(self.color)
w=wind(12,"red",123)
w.display()

