"""in previous we define the function by def keyword and followed by function name.what if i dont mention the function can i do that.if i dont mention a name it becomes anonymous.we can
create a function in pyhton called as anonymous functions. Functions without name or it will call them as lambdas.
"""
#square of a number.
def squ(n):
    return n*n
print(squ(5))

#we want to use function only once and dont want to define the name of the function and we want one expression which returning a value.
#we can pass functions to a function,so that means the way you pass values the way you pass objects, you can also pass functions because functions are objects in python.
from functools import reduce
l=lambda n:n*n #functions are objects, you need to assign it to someone now l represent the function now you can l in other function also.
res=l(2)
print("square of a number by lambda",res)

#add two numbers
f=lambda a,b:a+b
r=f(2,3)
print("addign two numbers using lambda",r)

#you can pass any number of arguments in a lambda function but it should be only one expression.
#lambda functions are syntically restricted to a single expression.

#lambda function can be used with three functions.1.filter() ,2.map(),3.reduce()


#filter,map, reduce.
#filter function will take a list and do filtering and give values.it takes a sequences and also returns a sequence. syntax-->filter(func,iterable)  iterable--sequence.
print("using filter")
nums=[2,1,4,5,3,6,7,91,10,9]
def even(num):
    return num%2==0
l=list(filter(even,nums))
print(l)

li=list(filter(lambda n:n%2==0,nums))
print(li)

#map:it is used when we want t0 change the value of every element of a list.syntax--> map(func,*iterable)
num=[1,2,4]
def squa(num):
    return num**2
re=list(map(squa,num))
print("using map",re)

result=list(map(lambda n:n**2,num))
print(result)
#reduce:it is used to reduce the number of values from a list. reduce() function belongs to a module known as functools.--->reduce(func,iterable[,initial])
nu=[1,2,3,4]
def add(a,b):
    return a+b
r=reduce(add,num)   #in this we pass two parameters.it will two values at a time
print(r)






#entire code.
n1=[1,2,3,4,5,6,7,8,9]
f=list(filter(lambda n:n%2==0,n1))
print(f)
m=list(map(lambda n:n**2,f))
print(m)
r=reduce(lambda a,b:a+b,m)
print(r)

