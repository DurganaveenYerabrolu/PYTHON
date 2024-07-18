#NUMPY
"""if you want to work with multidimensional array or if you want to perform some scientific calculations with array we use NUMPY package.
there are 6 ways to create a arrays in python.
1.array()  2.linspace()  3.logspace()   4.arange() 5.zeros() 6.ones()
2.linspace():
it is used to create an array with equal interval between the elements.it will takes 3 arguments start,stop,step( means no of parts you want to go for).if you dont mention the no of parts it will
take 50 parts.return evenly specified numbers over a interval.
3.arange():
it is used to create an array with equal interval between the elements.syntax:arange(start,stop,step( means size),dtype=None)
4.logspace():
in linspace(0,logspace() we create the parts.but in linspace the gap between the elements is fixed, in logspace the spacing between the two number would be depend on the log of it.
5.zeros(),ones():
i want to create an array of size n and by default all the values are 0.in that case we are using zeros()same 1-->ones()"""
#1
from numpy import *
arr=array([1,2,4,5]) #you also mention type also by default based on the values it will convert.
arr1=array([1,2],int)
ar1=array([1.5,5,4,6,5])#it will all values into float.
print(ar1)
print(arr1)
print(arr)

#2
a1=linspace(1,50,10,dtype='int')  #all these values are float because we break the range into 16 parts. dtype is optional.
print(a1)

#3
a2=arange(1,50,2)
print(a2)

#4
a3=logspace(1,40,50)
print("%.2f"%a3[0])    #we want only two values after decimal.for particular value.
#5
a4=zeros(5)
a5=zeros(5,int)
print(a5)
print(a4)

#6
a6=ones(5,dtype='int')  #0r directly you mention the dtype.
print(a6)
