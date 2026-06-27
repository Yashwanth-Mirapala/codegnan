'''
File handling
-------------
-->File handler isa object of a file to maintain several functions of a file like
creating,reading ,updateing and detailing the files...
----
-->Two ways to open a file
---------------------------
1.open()
eg:
any=open("demo.txt","r")
print(any.read())
any.close()
--------------------
syntax:
file handler = open("filename.txt","mode")
--------------------------
--------------------------
file handler.close()
---------
2.with open()
Syntax:
with(Keyword) open("file name","mode") as file handler:
                ------------------
                -----------------
Ex:
with open("demo.txt","r") as so:
    print(so.read())
with key word
-------
--> Using this with keyword no need to close the file in these lines , it will close the file automatically
Modes
--------
r --> used to the file and throw error if the file does not exist....
Ex:

a--> used  add the text at the last ,if the file does not exist it will creat the file
Ex:
with open("dem.txt","a") as so :
    print(so.write("Not feeling well"))

w--> used to add new text as override the text in the file, if the file does not exist creats the new file
Ex:
with open("dem.txt","w") as so :
    print(so.write("Not feeling well"))
    
x-->used to creat the file if the file exist it throw the error
Ex:
with open("yash.txt","x") as so :
    print(so.write("Yashwanth"))

read()
--------
--> The read method can read the entire file chunk by chunk we can spect
readline()
------------
--> tihs method can read one line at a time
with open("demo.txt","r") as so:
     print(so.readline())
'''

with open ("demo.txt","r") as so:
    print(so.readlines(     ))






 


