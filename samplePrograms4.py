n=int(input("enter"))
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

for i in range(n+1):
    print(fib(i),end=" ")
print("\n")

a=0
b=1
print(a,b,end=" ")
i=1
while(i<n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1
print("\n")  
def fact(n):
    if n<=0 or n==1:
        return 1
    else:
        return n*fact(n-1)

res=fact(n)
print(res)

fac=1
for i in range(1,n+1):
    fac=fac*i

print(fac)


n1=153
temp=n1
sum=0
while(n1!=0):
    re=n1%10
    sum=sum+(re)**3   
    n1=n1//10
if(sum==temp):
    print(temp,"is a armstrong number")
else:
    print(temp,"is not a armstrong number:")
