#ITERATION IN PYTHON:
"""iteration is the process of repeating a task or action multiple items. In programming is often used to process a sequence of data, such as string,list."""
"""
Iterators are used to access the elements of a sequence one at a time. this is useful for processing large sequences of data without having to store the entire sequence in memory."""
#iterator----it is used for iterations.

"""in for loop we have iterate between elements. so lets say if we have a list of 5 elements using a for loop we can iterate from the first element to the last element.
there are 3 ways for printing the sequence of values 1.using index, 2.using loops  3.iterator"""
#using index:
num=[1,2,4,5,7,8,9]
print(num[0])   #if you want to print numbers one by one we use index numbers.
print(num[1])

#using loop:
for i in num:
    print(i)

#using iterator:
"""in behind scene for loop as well what works is iterator."""

it=iter(num)  #the function which converts the list into iterate --iter()  

#iterator will not give all the values it will give one value at a time
print(it)   #it will give the object of iterator.
#we want values.  ---iter() will have inbuilt method __next__() it will give value(one value)
print(it.__next__())  #it will give 1
print(it.__next__())  #2
print(it.__next__())   #4
#same way as index values but the advantage is you dont have to use index values.you simply it.__next__().

"""behind the scene when you say iterator will have multiple values to you ,wil say hey iterator i am calling your method which is __next__(). it will pick one value.
again we call next, it knows the value of 'i' which means it will preserve the state of the last value, so it will the next value.
"""
#or
print(next(it))  #5

"""what if you want to create your own object.in the above they built in object(list).
the moment you say need your own object you need your own class.
I want to print top 10 values(1 to 10),one by one.
"""
class TopTen:
    def __init__(self):   #i want to define my own counter variable.
        self.nums=1
    def __iter__(self):
        return self         #this will give the object.
    def __next__(self):
        if self.nums<=10:
            val=self.nums
            self.nums+=1
            return val
        else:
            raise StopIteration

values=TopTen()
print(values.__next__())
for i in values:
    print(i)
