#how to reverse a list using for loop.
"""li=[1,2,4,5,6]
rev=li[::-1]
print(rev)
li.reverse()
print(li)

li=[1,2,4,5,6]
l=[]
i=len(li)-1
while(i>=0):
    l.append(li[i])
    i-=1
print(l)

li=[1,2,4,5,6]
lis=[]    
for i in range(len(li)-1,-1,-1):
    lis.append(li[i])
print(lis)


year=int(input("enter the year:"))
if (year%4==0 and year!%100==0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print("it is not a leap year")

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")
"""
#power set program in python
#all possible subsets of a given set including an empty set is known as power set.

size_set=int(input("enter the size of set:"))
set1=[input(f"enter{i+1} element:")for i in range(size_set)]
result=[[]]
for i in set1:           
    n=len(result)        
    for j in range(n):    
        r=result[j]+[i]   
        result.append(r)
for element in result:
    print(element)
        
    
