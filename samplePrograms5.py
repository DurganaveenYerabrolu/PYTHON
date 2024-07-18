#how to convert the list to string in python
#using JOIN method
"""mylist=["w","t"]
st=" ".join(mylist)
print(st)

#using join and map
list=["w","p","o",1]
mystr=" ".join(map(str,list))
print(mystr)

#using for loop
string= ""
for s in list:
    string= string+str(s)+" "
print(string)


#using list comprehension.
st=" ".join([str(s) for s in list])
print(st)


#string to list
string="ha ien mfkg"
lis=string.split(" ")
print(lis)

#check for vowels or consonants
str=input("enter the letter:")
str=str.lower()
if str=='i' or str=='e' or str=='i' or str=='o' or str=='u':
    print(f"{str} is vowel")
else:
    print("it is a consonant:")   

def check_vowel(string):
    new_string=string.lower()
    if len(new_string)>1:
        print("enter only one character:")
    else:
        vo=['a','e','i','o','u']
        if new_string in vo:
            return f"{new_string.upper()} is vowel"
        else:
            return f"{new_string.upper()} is not vowel"
character=input("enter the character:")
print(check_vowel(character))

#to filter odd and even numbers from the list
lis=[1,2,4,5,6,3,5,6,8]
even_list=filter(lambda n:n%2==0,lis)
even_list=list(even_list)
print(even_list)

odd_list=filter(lambda n:n%2!=0,lis)
odd_list=list(odd_list)
print(odd_list)

#using loop

even=[]
odd=[]
for i in lis:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


#using function.
def even_odd():
    even=[]
    odd=[]
    for i in lis:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    return even,odd
res=even_odd()
print(res)

#how to find the duplicates from the list in python.
list=[1,2,4,2,1,2,3,4,5,6,7,5,6,7]
li=[]
d=[]
for i in list:
    if i not in li:
        li.append(i)
    else:
        d.append(i)
print(d)
       
#by set
li=[1,2,4,5,2,2,1,3,4,5,7,8,9,10]
store_d=set()
for i in li:
    if li.count(i)>1:
        store_d.add(i)

store_d=list(store_d)
print(store_d)

#list Comprehension
duplicatelist=list(set(i for i in li if li.count(i)>1))
print(duplicatelist)


mystr=input("enter the string:")
mystr=mystr.lower()
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for char in mystr:
    if char in vowels:
        vowels[char]+=1
print(f"the number of vowels in the string are{vowels}")  """

#how to reverse a number in python
num=int(input("enter the number:"))
sum=0
while(num!=0):
    re=num%10
    sum=sum*10+re
    #print(sum)
    num=num//10
print(sum)


#another method slicing operator
num=113
num=str(num)
reversed_num=num[::-1]
re=int(reversed_num)
print(re)

n=45
re_num=int(str(n)[::-1])
print(f"reversed number is {re_num}")

#using function
def reverse(n):
    return int(str(n)[::-1])
n=1245
print(reverse(n))

