#RECURSION
"""calling a function itself.
To print a statement of a function multiple times,we can call a function inside the same function.
maximum limit for recursion is 1000 in python, so it will give an error after exceeding its limit.
if a code goes into recursion without a condition and it goes to infinite times, then it may hang the system and that limit set in python.
you can also print the limit of the recursion by using the function getrecursionlimit() available in the sys library.
you can change limit by using setrecursionlimit() function.
"""
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10)
print(sys.getrecursionlimit())

i=0
def great():
    global i
    i+=1
    print("hello",i)
    great()
#great()    #after execeeding limit it gives an error. 

