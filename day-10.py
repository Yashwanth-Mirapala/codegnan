'''
--> to remove the duplicates

so=eval(input())
empty_=[]
for i in so:
    if i not in empty_:
       empty_.append(i)
print(empty_)
    
'''

nums = [10,2,20,76,4,45,99]
max1=0
max2=0
for num in nums :
    if num > max1:
        max2=max1
        max1=num
       print(f"{max2} is gthe second laegest number in list{nums}")
