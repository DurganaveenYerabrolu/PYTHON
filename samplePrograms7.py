str="ddk ksk kfirej irii"
count=0
for i in str:
    if i.isalpha():
        count+=1
print(count)

#calculate the frequency of characters in python.
mystr=input("enter your string:")
temp=""
#this temp variable helps us to count the each character only once.
for char in mystr:
    if char not in temp:
        temp+=char
        print(f"{char}:{mystr.count(char)}")
    


 
#using while loop
st="ketfjf"
temp=""
i=0
while i< len(st):
    if st[i] not in temp:
        temp+=st[i]
        print(f"{st[i]}:{st.count(st[i])}")

    i+=1
#dictionary comprehension
char_count={char:st.count(char) for char in st}
print(char_count)


#sum of digits of numbers in python.
num=1223
sum_of_digit=0
while(num!=0):
    sum_of_digit+=num%10
    num=num//10
print(sum_of_digit)

n=input("enter:")
s=0
for i in n:
    s+=int(i)
print(s)



