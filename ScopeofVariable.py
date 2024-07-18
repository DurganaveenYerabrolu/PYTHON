#scope of a variable means where it can access the variable
#there are two types of scope of variable. 1.local scope 2.global scope.
#local scope :variables that are declare inside the function. the function destroy the variable after the execution complete.
def fun():
    a=10
    print(a)
fun()
#global scope :variables that are declared outside the function.can access every where.
b=10
def fun1():  #if the local variable is not declare then we can access global variable inside as well. 
    print("inside fun1 b=:",b)

fun1()
print("outside fun1 b=",b)

#local variable has the highest priority in accessing over global variable of the same name.
#if you want to access the global variable inside the function. and want to change the global variable inside the function we have to use global keyword.
c=10
def fun2():
    #my intention here to work with global variable not local variable.
    global c
    c=30
    print("inside fun2 C=",c)

fun2()
print("outside fun2 C=",c)    

#can we acess the local and global inside function at the sametime with same variable name----answer is NO
#if you want to use local variable but also we also change the global variable inside the function. we have special function called globals().using globals() we can access the global variable address
e=10
print(id(e))
def fun3():
    e=20
    x=globals()['e'] #it gives all the values not just one.we want one you specify ['variable name'].
    print(id(x)) #both have same address.
    #now modify global without effecting the local.
    globals()['e']=23
    print("inside fun3 e:",e)
fun3()
print("outside fun3 e:",e)
