#1.check for armstrong num or not
n=int(input("enter the number:"))
temp=n
sum=0
while(n!=0):
    re=n%10
    sum+=(re**3)
    n=n//10
if(sum==temp):
    print(f"{temp} is a armstrong number:")
else:
    print(f"{temp} is not a armstrong number")

#remove the duplicates from the list.
lis=[1,2,4,2,4,5,5,6,7]
dup=[]
for i in lis:
    if i not in dup:
          dup.append(i)
print(dup)
          


#using set.
l1=[2,4,4,3,2,4,5,6,7,8]
remo=set(l1)
remo=list(remo)
print(remo)


#printing duplicates elements from the list:
l2=[1,2,4,1,2,3,4,5,6,3,7,4,7,9,64]
l3=[]
l4=[]
for i in l2:
    if i not in l3:
        l3.append(i)
    else:
        l4.append(i)
print(l4)
    
