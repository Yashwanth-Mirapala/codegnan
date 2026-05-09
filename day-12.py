'''
num=0
num_1=1
Any=int(input("Enter the number: "))
print(num,num_1,end=" ")
for j in range(1,Any+1):
    num_2=num+num_1
    num=num_1
    num_1=num_2
    print(num_2,end=" ")

num=int(input("enter number:"))
total=0
num_2=len(str(num))
for j in str(num):
    total += int(j) ** num_2
if total== num :
    print(f"{num} is a Amstrong number")
else :
    print(f"{num} is not a Amstrong number")
 
odd=int(input("enter num: "))
for i in range (1,odd+1):
     
    if i %3 == 0 and i % 5==0 :
        print(f"{i} is divisible by 3 and 5")
    else :
        print(f"{i} is not divisible by 3 and 5")


sum_even_1=[40,20,36,7,9]
def sum_even(sum_even_1):
    total=0

    for j in sum_even_1:
        if j % 2 == 0:
            total += j
    print(total)
sum_even(sum_even_1)
            

Lambda function
-----------------
--> A lambda function is a small ananymus function
--> This lambda function can take n number of arguments but can only have one expresion
syntax --> lambda keywords (arguments) : expression


an = lambda a,b=a**b
print(an(5,6))
'''











