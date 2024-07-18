#factorial of a given number.
n=int(input("enter the factorial you want:"))
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of{n} is:",fact)

fac(n)


def facto(n):
    if n<0:
        print("enter the valid number:")
    elif n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)
for i in range(n,0,-1):
    print(f"{i}*",end="")
print("=",facto(n))

