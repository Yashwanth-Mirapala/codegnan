'''
Tuple
----------
-->Tuple is a collection of diffrent data types that represent by
() and the items in the tuple is seperated by commas
-->Tuple is immutable
ex:
so=(1,2,3,4,5)
tup=(8,7,6)
print(so + tup)

Dictionary
------------
--> dict ios a collection of key:value pair ,
where keys are immutable such as (string, int , tuple)
and values are any datatype
This is represented by {}

Methods
--------
keys()
this method is used to access only keys in the dictonery
syntax-->dict.keys()
Ex:
dic={"Name":"yash",
     'age' : 23,
     'edu' : "b tech"}

print(dic.keys() )
------------------------------------
values()
-->this is used to access only values in the dictonery
---> syntax : variable_name.values()
Ex:
dic={"Name":"yash",
     'age' : 23,
     'edu' : "b tech"}

print(dic.values() )
------------------------------------
items()
--> Thhis is used to access the key : values pairs in the dictonery
--> syntax : variable_name.items()
ex:
dic={"Name":"yash",
     'age' : 23,
     'edu' : "b tech"}

print(dic.items() )
-----------------------------------  
clear()
--> used to clear the entire dictonery which consist of all the items at a time
syntax--> dict.clear
Ex:

dic={"Name":"yash",
     'age' : 23,
     'edu' : "b tech"}

dic.clear()
print(dic)
------------------------------------
update()
--> this i9s used to add or update the new item () key : value )into the dict
syntax--> dict.update({"key" : "value"})
ex:

dic={"Name":"yash",
     'age' : 23,
     'edu' : "b tech"}

dic.update({"Role" : "Python Developer"})
print(dic)

'''






































































                                                          
