#count the number of vowels in a given string
#coonvert the vowels into Uppercase letters
str="hai welcome to giet engineering college"
count=0
ans=""
for i in str:
    if(i=="a" or i=="e" or i=="i" or i=="e" or i=="u"):
        ans+=i.upper()
        count+=1
    else:
        ans+=i.lower()
print(count)
print(ans)
#full form into shortform
str=input("enter the fullform:")
str=str.title()
sf=""
x=str.split()
for i in x:
    sf+=i[0]
print(sf)
#maximum number from the list
n=int(input("enter the number of items"))
list=[]
for i in range(1,n+1):
        j=int(input("enter the items:"))
        list.append(j)
print(list)
maxm=0
for i in list:
    if i>maxm:
        maxm=i
print("maximum number from the list",maxm)
print(max(list))
list.sort()
print(list[-1])

    
