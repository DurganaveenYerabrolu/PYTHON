#inner class
"""
instead of creating a class outside it also create inside class .(getting that group).
when you know that the class will be useed only for stdent(one class) nothing else, you dont have to create a seperate file that you can do that in student class itself.
you can create a object of inner class inside the outer class."""
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.Laptop()   #object create for inner classs(Laptop).
    def show(self):
        print(self.name,self.age)
    class Laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu='i5'
        def show(self):
            print(self.brand,self.cpu)


s1=student('dn',21)
s2=student('gh',34)
#calling the properties of inner class.
s1.lap.show()
#what if you want to create other object of it.
lap1=s1.lap
lap2=s1.lap    #for every object you will get different types of objects.
lap1.show() 
lap2.show()  


#create an object of inner class outside the outerclass provided you use outer class name to call it.
class st:
    pass
    class inner:
        def __init__(self):
            self.name="hai"
        def display(self):
            print(self.name)
s3=st()
lap3=st.inner()
lap3.display()
