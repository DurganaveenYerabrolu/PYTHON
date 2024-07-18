#convert decimal into binary in python.
bi=0b1010
print(bi)
b1=23
print(bin(b1))
n=int(input("enter the number:"))
b_list=[]
while(n!=0):
    re=n%2
    b_list.append(re)
    n=n//2
b_list=b_list[::-1]
print("binary of a given number is",end="")
for i in b_list:
    print(i,end="")

print()
#2.decimal to octal.
#using builtin function.
num=int(input("enter the number:"))
r=oct(num)
print(r)

h_list=[]
while num!=0:
    re=num%8
    h_list.append(re)
    num=num//8
h_list=h_list[::-1]
for i in h_list:
    print(i,end="")
print()
#decimal into hexa decimal.
dec_num=int(input("enter the number:"))
de=dec_num
hex_table={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
hex_list=[]
while dec_num!=0:
    re=dec_num%16
    hex_list.append(hex_table[re])
    dec_num=dec_num//16
hex_list=hex_list[::-1]
for i in hex_list:
    print(i,end="")
print()


e=hex(de)
print(e)
