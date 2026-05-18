'''
Inheritance
-------------
-->Inheriting  the method from the base to the child
Ex:
class parent:
    pass
class child(parent):
    pass
-----------------
single inheritance:
-----------------


class animal:
    def sound(self):
        print("Animals makes sound")

class dog (animal):
    def bark(self):
        print("Dog Bark")

D=dog()
D.sound()
D.bark()


Multiple inheritance:
--------------------
-->A child class inherits more than one class in called Multiple inheritance
EX:
class Father:
    def skill_1(self):
        print("Driving")
class Mother:
    def skill_2(self):
        print("Cooking")

class child(Father,Mother):
    def ALL_Skills(self):
        print("Gudisipodam")

c =child()
c.skill_1()
c.skill_2()
c.ALL_Skills()

-----Practice------ 

class Python:
    def skill_1(self):
        print("Python")
class Aptitude:
    def skill_2(self):
        print("Aptitude")

class DSA:
    def skill_3(self):
        print("DSA")
class SoftSkills:
    def skill_4(self):
        print("SoftSkills")
class Student(Python,Aptitude,DSA,SoftSkills):
    def All_skills(self):
        print("I have all these Skills")
s=Student()
s.All_skills()
s.skill_1()
s.skill_2()
s.skill_3()
s.skill_4()
-----------------------
Multi-level inheritance
-----------------------
-->Inherits from another child class
Ex:
class grandfather():
    def house(self):
        print("Grandfather's House")
class father(grandfather):
    def land(self):
        print("Father's land")
class son(father):
    def flat(self):
        print("Son's flat")
s=son()
s.house()
s.land()
s.flat()
--------------------
HierarchicAal inheritance:
----------------------------
Ex:
class father:
    def Property(self):
        print("FATHERS PROPERTY")
class child_1(father):
    def House(self):
        print("illu dengadu")
class child_2(father):
    def flat(self):
        print("flat dengadu")
class child_3(father):
    def bokka(self):
        print("House ,Flat Ammi dengadu")

s1=child_1()
s2=child_2()
s3=child_3()

s1.Property()
s1.House()


s2.Property()
s2.flat()

s3.Property()
s3.bokka()
---------------------
HYBRID INHERITANCE
--------------------
--> 
-->
--------------------
Super() :
--------------------
-->
Ex:
class parent:
    def __init__(self):
        print("Parent Constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = child()

'''
























