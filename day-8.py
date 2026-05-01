'''
elif statements
-----------------
marks=int(input("Enter Marks: "))
if marks >=90 :
    print("A+")
elif marks >=80 :
    print("A")

elif marks >=70 :
    print("B+")
elif marks >=60 :
    print("B")
elif marks >=50 :
    print("C+")
elif marks >35 :
    print("D")
else :
    print("Failed")
------------------------
Nested if :
---------------
--> if statement inside another if statement is called nested if
user_info= {"ATM PIN" :"8639"}
user_pin=input("Enter your ATM pin: ")
if len(user_pin)== 4 :
    if user_pin in user_info['ATM PIN'] :
        print("welcome")
    else :
        print("ENTER CORRECT PIN")
else :
    print("ENTER 4 DIGIT PIN")
------------------------------------------
for statement
------------------------
-->this statement is used to iterate over items like (string,list,tuple)with fixed number of itterations ;
any= [1,2,3,4,5]
for j in any :
    print(j)
-------------------
else statement :
-------------------
--> after completing all iterations this else statement will excicute 
any= [1,2,3,4,5]
for j in any :
    print(j)
else :
    print("loop finished")

#palendrome
so=input("Enter name : ")
kali=""
for j in so :
    kali= j + kali
if kali == so :
       print("Palindrom")
else :
       print(" Not a Palindrom")
'''


































