#fibonnaci series.
def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid, enter positive number:")
    elif n==1:
        print(a)
    else:
        print(a,b,end=" ")
        for i in range(2,n):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
            
                
n=int(input("enter the number:"))
fib(n)
print()

a=0
b=1
print(a,b,end=" ")
i=2
while(i<n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1
print()    
def fibb(n):
    if n<0:
        print("invalid:")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
for i in range(n):
    print(fibb(i),end=" ")
