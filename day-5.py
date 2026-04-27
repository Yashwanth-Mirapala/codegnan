
'''
List & Data type
--------------------
list is a collection of diffrent datatypes and it is representated by []
seprerated by comma (,)
EX:
any=[1,"python is a language",67,68,[34,["this is python class"],78,"I'm looking for a good bat"],[2,"this is 5th class",3],56]
print(any[4][1][0][14])

Methods :
---------------
1.append()
-->THis method is used to add new item into the list but it will add in the last index position
syntax --> 
variable_name.append()

Ex:
app=[1,2,3,4,5]
app.append(6)
print(app)
app.append([0,9,8,7])
print(app)
-------------
2.extend()
-------------
--> this method is also used to add new item into the list but this extend add as each positon to each index in the list
--> extend oly takes itterables
syntax --> 
variable_name.extend(itterables)

Ex:
ext=[1,2]
ext.append("Python")
ext.extend("Python")
print(ext)
----------------
3.remove()
--> this also used to delete item from the list ,but remove() method will delete direct value
syntax --> 
variable_name.remove(value)
Ex:
rem=[1,2,3,4]
rem.remove(3)
print(rem)
-----------------
4.pop()
--> it is used to delete the item from the list
--> it removes only based on the index position mentioned in the parameters
--> if notting is mentioned in the perameters, it will remove last index position value
syntax --> 
variable_name.pop(index position)

Ex:
pop=[1,2,3,4]
pop.pop(3)
print(pop)
--------------
slicinng()
--------------
--> this is used to get the particular part of the list ,string or tuple
--> this will work based on index position

syntax --> variable_name[starting index: ending index ]
Ex:
sli=[1,2,3,4,5,6,7]
print(sli[2:5])
-------------------
len()
index()
count()
insert()
--------
-->

'''

































