#arrays in python
"""Arrays:arrays means all the values of same type. Arrays in python have do not have fixed size.which means we can expand,shrink etc.
we will not getting a array by default.we need to import module. """
#import array as arr
#val=arr.array('i',[1,2,3])
#print(val)
"""while creating an array we have to mention 2 things.
1.type code (type of the values)
2.mention the values."""
from array import *
vals=array('i',[1,2,3,4,5])
print(vals)
v=array('f',[1.2,3.4,5.6])
print(v)
v1=array('I',[3,1])
print(v1)
print(vals.buffer_info()) #return the size (adderss,size)
vals.append(6)
print(vals)
print(vals.count(1))
print(vals.index(1))
vals.extend([1,2,3]) 
print(vals)
vals.remove(1)  #remove the first occurence of value.
print(vals)
vals.reverse()
print(vals.typecode)
print(vals.itemsize)
print(vals)
for i in vals:
    print(i)
    
#taking elements from the user.
n=int(input("enter the number:"))
ar=array('i',[])
for i in range(1,n+1):
    a=int(input("enter the elements:"))
    ar.append(a)
print(ar)

#create a newArray and copying from another array.
newArray=array(ar.typecode,(a for a in ar))
print(newArray)

#search an element;
s=int(input("enter element to be search:"))
for e in newArray:
    if e==s:
        print("element found ")
        break
    else:
        print("element not found:")
        break
#BY index, which index the element is found.
k=0
for t in newArray:
    if t==s:
        print("element found at",k)
        break
        k+=1
    else:
        print("element not found:")
        break
#Using function.
val=int(input("enter the number which in the array and we found the index."))
print(newArray.index(val))
