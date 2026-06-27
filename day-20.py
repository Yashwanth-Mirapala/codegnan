'''
Regxex or regular expressions is a sequence of charectersthat forms a serching pattern
To use this Regex we have to import package called re
Syntax: import re
Functions
----------
findall()
search()

Metacharecters
--------------
-->
1.[]-->a-z,A-Z,[ahg]
EX-1
import re
some="Python is a language"
any=re.findall("[a-z]",some)
print(any)
EX:2
import re
some="Python is a language"
any=re.findall("[ati]",some)
print(any)
Ex:3
import re
some="Python is a language"
any=re.search("[ati]",some)
print(any)

2:dot: "."
--> IT will take any char , but one dot is one char
Ex:
import re
some="Python is a language"
any=re.findall("P..h..",some)
print(any)

3:"^"
--> checks the string is starting with or not
EX:
import re
some="Python is a language"
any=re.findall("^P..h..",some)
print(any)

4:"$"
Ex1:
import re
some="Python is a language"
any=re.findall("language$",some)
print(any)
Ex2:
import re
some="Python is a language"
any=re.search("language$",some)
print(any)

4:".*"
EX 1:
import re
some="Python is a language"
any=re.findall("P.*",some)
print(any)
Ex2:
import re
some="Python is a language"
any=re.findall("P.*n",some)
print(any)

5:"+"
Ex:
import re
some="Python is a language"
any=re.findall("P.+on",some)
print(any)

6:"{}"
Ex:
import re
some="Python is a language"
any=re.findall("P.{19}",some)
print(any)
 



import re
some="Python is a language"
any=re.findall("P.{19}",some)
print(any)

'''
import re
def Validate_name(name):
    pattern = "[]"



















