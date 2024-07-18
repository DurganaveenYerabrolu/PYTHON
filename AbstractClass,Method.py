#ABSTRACT CLASS:
"""abstract class can be considered as a blue print for other classes. it allows you create a set of methods that can be created within any child classes built from the abstract class.
A class that contains one or more abstract methods is called an abstract class.
A abstract method is a method that has declaration but does not have an implementation.
#we use abstractclass for while we are designing large functional units or when we want to provide a common interface for different implementations of a component."""
#ABSTRACT BASE CLASSES in Python:
"""by defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where a third
party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code base area where keeping all classes in your mind is
difficult or not possible."""
#WORKING On Python Abstract Classes:
"""by default, python does not provide abstract classes. python comes with a module that provides the base for defining Abstract Base Classes(ABC) and that module name is ABC.
ABC works by decorating methods of the base class as an abstract and then registering concrete classes as implementations of the abstract base.
A method becomes abstract when decorated with the keyword @abstractmethod.   """
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod     
    def show(self):    #you can't create a object for abstract class because you have a method which is not define. abstract class contain normal methods also
        pass                    
class B(A):        #its responsibility is to define(implement) all the methods that are declare in the abstract class.
    def show(self):
        print("hello printing...")

b=B()
b.show()

#simply, an abstract class is a class that cannot be instantiated and typically contain abstract methods,which are methods with out implementation.
#subclsses must provide implementation for these abstract methods.
"""we create a class(sub class) that class will implement all the abstract methods, if you fail to implement all the abstract methods you will get an error. """
class student(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(student):
    def process(self):
        print("executing...")
class programmer:
    def work(self,com):
        print("coding...")
        com.process()
pro=programmer()
com1=Laptop()
pro.work(com1)
