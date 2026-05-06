'''

Functions
-----------
-->THis is a block of code that can be reusable
--> A Function can only run when it is called
--> def id the keyword used to define the function
Syntax:
def function_name (parameters) :
    ---------
    ---------
function_name(argument)
Ex:
num=8
def even_odd(num):
      if num % 2==0 :
            print(f"{num} is even number")
      else :
            print(f"{num} is odd number")
even_odd(num)
even_odd(247) 

Required ar :
--> A Function must called with the correct number of arguments ,
that means if function expectx 2 arguments ,
we have to call the function with 2 arguments not less or not more
Ex :
def man (num,num_):
      print(num + num_)
man(9,8)

Default argument :
-->BY default, value is tacken from the calling function
def name(name="yash"):
      print(f"Hii {name}")
name("satya")
name("sriram")
name()

keyword Arguments
-----------------
-->Here, we can send argumnt with key = Value syntax .
By this , the order of the argument doesnot matter
Ex:
def numbers(num,num_2,num_3):
      print(num_2+num_3+num)
numbers(num_2=3,num_3=2,num=1)

Variable length argument:
-------------------------
-->Adding a star (*) before the parameter name to they function ,
receave a tuple of arguments and can be Access items with the indexs
EX:
def Yashwanth(*name):
      print(name[0])
Yashwanth("yash", "staya","sri","ram")

'''





















