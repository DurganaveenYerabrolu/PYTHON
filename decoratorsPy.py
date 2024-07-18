#decorators
"""by using decorators you can add extra features in the existing functions.
by decorators we can change the behaviour of the existing function at the compile time itself."""
def div(a,b):
    print(a/b)
div(4,2)

div(2,4)
"""i want it doesn't matter in sequence pass the value it should be bigger than denominator. if not i want swap a,b values."""
def div1(a,b):
    if a<b:
        a,b=b,a
    print(a/b)
div1(2,4)
""" this code which you have here is not with you this is in some other file and you are importing it may be you don't have the access for this function and you dont want to change
the code of the existing function so i want those two values without touching the function.that where decorators comes into the picture."""
def div2(a,b):
    print(a/b)
def smart_div(func):   #this is a decorator for div. which except a function as a parameter this is actually div2 function.
    #i want to change the logic i want write a logic in the another function.(inner function)
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner
div2=smart_div(div2)
div2(2,4)
    
