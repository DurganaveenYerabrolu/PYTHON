"""formal arguments :when define it, it is formal.    def fun(a,b):
actual arguments: when you passing the value, when you are calling it is actual argument. fun(2,3)
actual arguments are classified into four types.
1.positional arguments    2.keyword arguments 3.default arguments 4.variable length arguments
1.
"""
def fun(a,b):
    c=a+b
    print(c)
fun(1,2)  #during the function call,values are passed to the arguments should be in order to the arguments in the function defintion.
2.
#same but should not be order.all keyword arguments should match the parameters in the function definition.
def fun1(a,b):
    c=a+b
    print(c)

fun1(b=30,a=1)

#3.default arguments are values that are provided while defining functions.if we provide a value to the default arguments during function call then it override the default value.
#default arguments should follow non default arguments.(non default argument follows default argument)
def fun2(ag,name="jd"):
    print(name,ag)
fun2(2)

#4.if you want to pass multiple value in a function call we can use variable length arguments.
def fun3(a,*b):  #*b stores the values in tuples
    print(a)
    print(b)
    #add all the vlaues.
    c=a
    for i in b:
        c+=i
    print(c)

fun3(1,2,3,4,5)
#keyword variable length arguments.
#it is a feature that allows a function to accept an arbitary no of keyword arguments.
def fun4(**data):
    for i,j in data.items():
        print(i,j)
fun4(name="dn",age=22,rollno="5A2")
