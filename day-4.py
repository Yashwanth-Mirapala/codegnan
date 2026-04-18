#data-types
          #mutable                      #imutable
'''Mutable-Datatype
-------------------------
In Python, a mutable data type is one whose internal state or contents can be changed after it has been created
without changing its identity.

--->example
Common Mutable Types
---------------------
Lists: [1, 2, 3] (can append or change items).

Dictionaries: {"a": 1} (can add or update keys).

Sets: {1, 2, 3} (can add or remove elements).

Bytearrays: A mutable version of bytes.
---> immutable data type
----------------------------
An immutable data type is one whose content or state cannot be changed after it is created.
If you attempt to modify an immutable object, Python creates a completely new object in memory with the new value.

Key Characteristics
Fixed State: Once defined, the data inside the object cannot be altered.

Hashable: Because they don't change, most immutable types can be used as keys in a dictionary.

Memory Behavior: Modifying the variable results in a new memory address (id()).

---> examples Common Immutable Types
------------------------
Numbers: int, float, complex.

Integer (int)
---------------
Whole numbers without decimals.

Example: x = 10

Behavior: If you do x += 1, Python creates a new integer object 11 and assigns x to it.
The original 10 remains unchanged in memory until cleared.

2. Float (float)
------------------
Numbers containing a decimal point.

Example: price = 99.99

Behavior:
Changing the price to 100.0 doesn't modify the existing float; it allocates a new space in memory for the new value.

3. Complex (complex)
--------------------
Numbers with a real and an imaginary part (denoted by j).

Example: z = 3 + 5j

Behavior: You cannot modify z.real or z.imag directly. To change the value, you must redefine the entire variable.

Strings: String is a collection of charecters that are enclosed in ('',"",''' ''') it is immutable datatype
"hello" (you cannot change a single character in-place).

---------
Tuples: (1, 2, 3) (a fixed sequence).
--------
Frozen Sets: An immutable version of a set.
-----------
Bytes: Immutable sequences of single bytes.
---------

'''
'''
indexing
-------------------------
---> this is used to get particukar substring ,item from string,list and tuple bycalling with index position
print(Syntax: variable_name[index_position])
ex:
any="python is a "
print(any[9])

concadination :
-------------------
a + acts as diffrent ways , if we are addingn two integers it acts like addition
in other cases such as list , string and tuple it acts like concadination
Ex:
any="Yashwanth"
an="Mirapala"
print(any+an)

# String Methods :
'''
'''
replace():
----------------
this method is used to replace the old  sub sting with new sub string
variable_name.replace("old string","new string ")
EX:
py = "bhargav kiran mutchu"
print(py.replace("bhargav kiran mutchu","Mbk"))
print(py)

split():
---------------
--->this method is used to seperate the string using the substring and it will split
into list such that before the substring is one index and after the substring
is another index
syntax ;
variable_name.split("substring")
Ex:
py = "bhargav kiran mutchu"
print(py.split( " ")) 

strip()
----------------------
--> This method is usedto remove first index position or last index position
syntax:
variable_name.strip("substring")
Ex:

py = "bhargav kiran mutchu"
print(py.strip( " mutchu"))

join()

lower()
upper()

'''

py = "bhargav kiran mutchu"
print("-" .py(strip))




