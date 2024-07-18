season=input("enter the season:")
if season=="summer":
    print("Buy AC")
elif season=="winter":
    print("Buy RainCoat:")
elif season=="rainy":
    print("Buy Blanket")
else:
    print("invalid: enter seasons summer,winter,rainy:")

#biggest of three numbers:
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if a>b and a>c:
    print(a,"a is big:")
elif b>c:
    print(b,"b is big:")
else:
    print(c,"c is big:")

phy_marks=int(input("enter the p:"))
che_marks=int(input("enter the c:"))
Math_marks=int(input("enter the M:"))
if phy_marks>=35 and che_marks>=35 and Math_marks>=35:
    print("Pass:")
else:
    print("Fail:")
#to print "valid" if the given password has greater than or equal to 8 otherwise print "not valid"
password=input("enter the password:")
if len(password)>=8:
    print("Valid:")
else:
    print("Not Valid:")
#print how many 100 rupee notes,50 notes and remaining change in the given amount
amount=int(input("enter the amount:"))
notes_100=amount//100
print("100 notes",notes_100)
remain_100=amount-(notes_100*100)
notes_50=remain_100//50
print("50 notes",notes_50)
remain_50=remain_100-(notes_50*50)
print("remaining Change:",remain_50)
