#USER INPUTR IN PYTHON
#the input function is used to accept user input from the command line or console.it always returns a string, regardless of what the user enters.
#eval function
#eval() function is used to evaluate an expression entered by the user as a string.it returns the result of the expression as  a value.
#passing values from the command line
#sys module provides access to any commandline arguments via the sys.argv list.
import sys
i=input("enter 1:")
j=input("enter 2:")
print(i+j)
#char
ch=input("enter the char")[0]
print(ch)

#eval
res=eval(input("enter the expression"))
print(res)
#taking input from the command line.i want to pass value when iam running(cmd).argv has multiple values to acess this value we use index number.
#we runit on cmd 
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)
