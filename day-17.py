'''
def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

def ams(num):
    temp=num
    digits=len(str(num))
    total=0

    while temp>0:
        digit=temp%10
        total=total+(digit ** digits)
        temp=temp // 10
    if total==num:
        return True
    else:
        return False
num_=int(input("Enter Num: "))
if ams(num_):
    print(num_,"Its amstrong Number")
else :
    print(num_,"it is not a amstrong Number")
'''
def rev(text):
    rever=" "
    for i in text:
        rever=i + rever
    return rever
word=input("Enter yor Name: ")
result=rev(word)
print("your result: ",result)
