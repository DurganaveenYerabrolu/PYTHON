#COPYING AN ARRAY IN PYTHON
#normal problems
#add two arrays
from numpy import *
arr1=array([1,2,4,5])
arr2=array([2,3,4,5])
arr3=arr1+arr2    #vectorized operation
print(arr3)

ar=arr1+5 #adding an element to all elements in an array.
print(ar)
#we want to concentate two arrays.
print("concatenating two arrays:")
print(concatenate([arr1,arr2]))
#copy
a1=array([1,2,3])
a2=a1
print(a1)
print(a2)
#a1,a2 both are different variables both pointing to same memory(same address) .[aliasing].i dont want have same array.i want to create new array 1 array takes different address another take different address.
#we use view():
#view() is a function used to create a new array with different location.
arra1=array([1,2,4,6,7])
arra2=arra1.view()
arra1[0]=2
print(arra1)
#print(id(arra1)) you can check with id() function.
print(arra2)

#Copying Types:
"""shallow copy()--it simple copy the element both the array ask to depend on each other.when we change the value in ar1 then it automatically also change the value in ar1.
#deepcopy()
two different arrays  which do not link with each other any way.
"""
aray1=array([1,3,4,5])
aray2=aray1.copy()
aray1[0]=2
print(aray1)
print(aray2)
