'''
user input :
---------------
--> int data type
me= int (input("enter a number: "))
print(type(me))

--> passing two values
a,b=map(int,input("Enter the numbers").split())
print(a)
print(type(a))
print(b)
print(type(b))
--------------------

--> string data type
any=input("enter the word: ")
print(type(any))
---------------------
--> list data type
li=list(map(int,input("enter the number").split()))
print(li)
print(type(li))
-------------------
--> tuple data type
ti=tuple(map(int,input("enter the number").split()))
print(ti)
print(type(ti))

-->f"strings"
d=79
r=49
print(f"d+r= {d+r}")
print(f"{d} + {r} ={d+r}")
if statement
------------------
this is used to check condition is true or not
num=40
if num<= 40 :
    print(f"num is less than")
else statement
-----------------
--> else is a fall back statement, incase of statement because false, it will enter into else

num=40
if num<= 40 :
    print(f"num is less than")
else :
    print(f"num is greater than 40")
---------------------------------------
-->finding the greater number
a=80
b=60
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a} ")
---------------------------------------
#eval
E=eval(input("Enter:"))
print(type(E))
print(E)
---------------------------------------
Marks=int(input("enter your Marks: "))
if Marks>=35:
    print("you are pass")
else:
    print(f"you are fail")
---------------------------------------    
age=int(input("entr your age: "))
if age>=35:
    print("you are eligible to vote")
else:
    print(f"you should waite {18-age} years to vote")

'''























    
 
