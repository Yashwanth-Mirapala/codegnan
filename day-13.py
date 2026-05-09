
'''
indu_union_ac_details={"Name":"indu","ATM_PIN":"8008","Balance":7000}
print("---------------WELCOME TO UNION  BANK------------------------")
print("Please insert your card")
user_pin = input("Please enter your 4 digit pin:")
if len(user_pin) == 4:
    if user_pin in indu_union_ac_details["ATM_PIN"]:
        Choice_ = int(input("\n1.Withdraw \n2.Deposite: "))
        if Choice_ == 1:
            Withdraw_M = int(input("Enter amout  you want to withdraw: "))

            if Withdraw_M <= indu_union_ac_details['Balance'] and Withdraw_M:
                indu_union_ac_details['Balance'] -= Withdraw_M
                print("Please wait unlike money process")
            else:
                print("Insuffient funds or change is not getable")
        elif Choice_== 2:
            deposit_m = int(input("Enter amount to deposit: "))

            if deposit_m >= 1000 and deposit_m%100 == 0:
                indu_union_ac_details['Balance'] += deposit_m
                print("Amount deposited successfully")
                print("Updated Balance:", indu_union_ac_details['Balance'])
            else:
                print("Invalid amount")
            
       
    else:
         print("Please enter correct pin")
else:
    print("Please enter only 4 digit pin")

list_comprehension
---------------------
-->List comprehension offers shorter syntax when we want to creat a new list based on the values of the existing list
syntax --> [expression loop condition]


odd=[1,2,3,4,5,]
even=[i for i in odd]
print(even)

old=[1,2,3,4,56,6,7]
new=["even" if i%2==0 else i for i in old]
print(new)

old=[1,2,3,4,56,6,7]
new=["odd" if i%2!=0 else i for i in old]
print(new)

--> Dictonery comprehension
---------------------------
--> DIctonery comprehension offers a short syntax when we want to creat a new dict based on the values of an exixting dict.

'''
dic={"a":2,"b":3,"c":4}
dic_1={x:y for (x,y) in dic.items() if y%2==0}
print(dic_1)

