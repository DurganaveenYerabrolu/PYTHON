"""#1.print numbers from 1 t0 100.
for i in range(1,101):
    print(i,end=" ")
print()
    
i=1
while(i<=100):
    print(i,end=" ")
    i+=1
print()
print([i for i in range(1,101)])
#2.python program to add two numbers.
a=10
b=10
c=a+b
print(f"sum of {a} and {b} is {c}")
print(f"{a}+{b} is {c:.2f}") 

#3.sum of natural numbers in python.
n=100
i=1
sum=0
while(i<=100):
    sum+=i
    print(i,"+",end=" ")
    i+=1
print("=",sum)
print()
sum=0
for i in range(1,101):
    sum+=i
print(f"sum of 1 to 100 is {sum}")

def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
    
n=int(input("enter the number:"))
print(f"sum of 1 to {n} natural numbers is:{sum(n)}") 
 
#4.sum of even numbers in python
i=0
sum=0
while(i<=100):
    if i%2==0:
        sum+=i
    i+=1
print(f"sum of even number from 1 to 100 is{sum}")

total=0
for i in range(0,101,2):
    total+=i
print(f"using for loop sum of even numbers is:{total}")


def even(n):
    s=0
    for i in range(1,n+1):
        if i%2==0:
            s+=i
    return s
n=int(input("enter the number:"))
print(f"by function sum of even numbers is:{even(n)}")  

#5.print even numbers from 1 to n:
n=int(input('enter the number:'))
for i in range(1,n+1):
	if i%2==0:
		print(i,end=" ")
print(" ")
for i in range(0,n+1,2):
	print(i,end=" ")
print()

i=1
while(i<=n):
    if i%2==0:
        print(i,end=" ")
    i+=1
print()
#in a given range.
n1=50
n2=100
while(n1<=n2):
    if n1%2==0:
        print(n1,end=" ")
    n1+=1
print()   

#6print odd numbers from 1 to 100.
i=1
n=100
while(i<=100):
    if n%2!=0:
        print(i,end=" ")
    i+=1
print()
for i in range(1,101,2):
    print(i,end=" ")
print() 

#7.how to remove the Punctuations in python.
#Punctuation:Punctuation marks are special symbols, such as full stops, commas, question marks, exclamation points, and more,used in writing to separate sentences and clarify meaning.
sentence=input("enter the sentence:")
punctuations="`~!@#$%^&*()-_=+;:'/,.><\"[]{}|?"
new_string=''
for i in sentence:
    if i not in punctuations:
        #new_string+=''.join(i)
        new_string+=i
print(new_string)
import string
def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)
sentence=input("please enter the sentence:")
print(remove_punctuation(sentence))  
#8.simple calculator in python.
expression=input("enter the expression")
result=eval(expression)
print(f"{expression}={result}")

def calculator(exp):
    return eval(exp)
e=input("enter the expression")
print(f"{e}={calculator(e)}")

#multiplication table
num=int(input("enter the number:"))
n=int(input("enter upto how many numbers you want"))
i=1
while(i<=n):
    print(f"{num}X{i}={num*i}")
    i+=1

for i in range(1,n+1):
    print(f"{num}X{i}={num*i}")

def multi(num):
    n=12
    for i in range(1,n+1):
        print(f"{num}X{i}={num*i}")


multi(10)  """
 #10.DISPLAY CALENDAR.
import calendar
year=int(input("enter a year:"))
month=int(input("ente a month:"))
print(calendar.calendar(year))
#display a specific month from calendar
print(calendar.month(year,month))

            

    
