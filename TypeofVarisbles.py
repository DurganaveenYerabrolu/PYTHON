"""variable are two types 1.instance variables, 2.class variables.
The variables that are define in the init then the variables are called instance variables.
you want to define the variable outside the init and inside the class then the variables are called class variables.
instance variables are different for different objects, while if you change one object it will not affect other objects.as object changes the values also change."""
class car:
    def __init__(self):
        self.mil=10
        self.com="bmw"        #instance variables ,stored in instance namespace.
c1=car()
c2=car()
c1.mil=8     #it will not affect other objects.
print(c1.com,c1.mil)
print(c2.com,c2.mil)

#in class variables if you change one variable then it will affect all the object they shared.when the class is define which is common for all the objects.
class car1:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="bmw"        
c3=car1()
c4=car1()
car1.wheels=6  #it will all the object they shared
print(c3.com,c3.mil,c3.wheels)
print(c4.com,c4.mil,c4.wheels)
    
