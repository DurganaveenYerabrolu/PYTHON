#how to check if a list is empty in python.
"""mylist=[1,2,4]
if mylist:
    print('list is not empty')
else:
    print('list is empty:')

if  not mylist:
    print('list is empty')
else:
    print('list is not empty:')

#USING ==
if mylist==[]:
    print("list is empty:")
else:
    print("list is not empty:")
    
#using len()
if len(mylist==0):
    print("list is empty")
else:
    print("list is not empty:")
    

list=[]
if len(list)>0:
    print("list is not empty:")
else:
    print("list is empty:")

#2.program to check whether the given number is even or odd
n=int(input("enter the number:"))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")


        
def even_odd(n):
    if n%2==0:
        return f"{n} is even"
    else:
        return f"{n} is odd"
#print(even_odd(n))
res=even_odd(n)
print(res)


#3.sort words in a alphabetic order.
words=input("enter the sentence:")
words=words.lower()
word_list=list(words.split())
#print(type(word_list))
word_list.sort()
sorted_words=" ".join(word_list)
print(sorted_words)

#li=['hai','er']
#print(type(li))
#li.sort()
#print(li)

#using function
def word(w):
    #return sorted(w.lower().split())  #return list type.
    return " ".join(sorted(w.lower().split()))
wi=input("enter the sentence:")
print(word(wi))

#4.connvert celsuis to fahrenheit in python.
#formula fahrenheit=(celsuis*(9/5))+32
c=float(input("enter the temperature in celsuis:"))
f=(c*(9/5))+32
print(f"temperature of {c} in fahrenheit is {f:.2f} F")

def temp(c):
    return (c*(9/5))+32
print(f"fahreheit is{temp(c):.2f} F")   

#5.sort a list without using sort() function in python
list=[1,2,5,0,6,4]
temp=0
for i in range(0,len(list)):
               for j in range(0,len(list)):
                    if(list[i]<list[j]):
                           temp=list[i]
                           list[i]=list[j]
                           list[j]=temp
print(list)
   
#using functions
def fun(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if list[i]<list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return f"the sorted set is{list}"
res=fun(list)
print(res)   """

#6.to find the numbers divisible by another numbers.
n=int(input("enter the size of list:"))
num=[]
res=[]
for i in range(n+1):
    nums=int(input("enter the numbers:"))
    num.append(nums)
div=int(input("enter the number we wish to check for divisibility:"))
for i in num:
    if i%div==0:
        res.append(i)
print(f"the numbers by{div} in the list are {res}")
        

#another way
len_list=int(input("enter the size:"))
num_list=[int(input(f"enter {i+1} elements:")) for i in range(len_list)]
d=int(input("enter a number we wish to check for divisibility:"))
result=[]
for i in num_list:
    if i%d==0:
        result.append(i)
print(result)

len=int(input("enter the size:"))
li=list(map(int,input()))
ns=int(input("enter divisibility you want check:"))
r=list(filter(lambda i:i%ns==0,li))
print(f"numbers divisible by{ns} are:{r}")





                    
                  
