stu=[]
sc=[]
n=int(input("enter no of records"))
for i in range(n):
               name=input()
               score=float(input())
               stu.append([name,score])
               sc.append(score)

s=set(sc)
li=list(s)
li.sort()
ans=li[1]
ans_list=[]
for i in stu:
      if ans in i:
          ans_list.append(i)
ans_list.sort()
for i in ans_list:
    print(i)
               
               
            
