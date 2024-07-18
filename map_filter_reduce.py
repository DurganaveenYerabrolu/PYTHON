import functools
#MAP()
#map function is used to apply a specified function to each item in an iterable(like a list,tuple etc)and return a new iterable containing the result.syntax map(function,iterable)
def squares(x):
    return x*x
res=map(squares,[1,2,4,5])
print(list(res))

#filter
"""filter function is used to filter elements from an iterable(like list,tuple)it return an iterable containing the elements for which the function return trues"""

def even(x):
    return x%2==0
re=filter(even,[1,2,4,5,6,8])
print(list(re))

#reduce
"""it is a part of functools module and it is used to apply a function of two arguments cummalatively to item of an iterable from left to right,so as to reduce the iterable to a single value."""
def fun(x,y):
    return x*y
res1=functools.reduce(fun,[1,2,3,4,5])
print(res1)
