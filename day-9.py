'''
While statements
-------------------
--> This while statements will keep on excicutoing intil unless condition becomes true
eX:
v=1
while v<=5 :
    print(v)
    v+=1
--------------
range()
--> This range function will generate themsequence of the numbers upto the limmit
Syntax:
range(starting,ending,step)
Ex:
wish=int(input("enter your limit : "))
for j in range (1,wish+1,2):
            print(j)
ex:
for y in range(2,101):
    if y % 2==0:
        print(f"{y} is the even number")
    else:
        print(f"{y} is a odd number")
---------------------
#control statements
break
-----------
-->This break statements will exit if the condition becomes true, and never enters into next loops
Ex:
any=["Miarapala","yashwanth","satya","sri","ram"]
for m in any:
    if m =="sri":
        break
    print(m)
--------------
continue:
--------------
--> This statement will skip the particular itteration and goes to the next itteration
Ex:
any=["Mirapala","yashwanth","satya","sri","ram"]
for m in any:
    if m =="Mirapala":
        continue
    print(m)
------------
pass
--------------
-->pass is a place holder , holds the space not to get any  error
Ex:
a=9
b=90
if a>=b:
    pass
-----------------
prime number
-------------
Ex:
num = int(input("Enter number: "))
cou=0
for i in range(1,num+1):
    if num % i == 0 :
      cou += 1
if cou==2 :
    print(f"it is a prime number")
else:
    print(f"it is not a prime number")
-------------------------
Nested loops
------------------
-->Loop inmside the loop is called nested loop
Ex:

'''
for j in range(2,100):
    count=0
    for i in range(1,j+1):
        if j % i == 0:
            count +=1
    if count==2 :
        print(f"{j} It is a prime number")
    else :
        print(f"{j} It is not a prime number")
                   








































