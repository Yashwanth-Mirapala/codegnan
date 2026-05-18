
'''
class
-----
class is instance or blue print of an object

object
------
object is a instance of class


class student:
    def display(self):
        print("peddi pahilwan")
s1=student()
s1.display()

constructer
-----------
a constructer is a special method that exicutes autometically when the object is created
EX:
class car:
    def __init__(self,color,Brand,Model,Varient):
        self.color = color
        self.Brand=Brand
        self.Model=Model
        self.Varient=Varient
    def car_brand(self):
        print(f"Brand is {self.Brand}")
        
    def car_color(self):
        print(f"color is {self.color}")
        
    def car_Model(self):
        print(f"Model is {self.Model}")
        
    def car_Varient(self):
        print(f"Varient is {self.Varient}")


car_1=car("Black","Audi","2026","Petrol")
car_1.car_brand()
car_1.car_color()
car_1.car_Model()
car_1.car_Varient()


self:
-----
--> This self refers to the current object
Ex:
class student:
    def __init__(self,name,section,sub,marks,year):
        self.name=name
        self.section=section
        self.sub=sub
        self.marks=marks
        self.year=year
    def stu_det(self):
        print(self.name)
        print(self.section)
        print(self.sub)
        print(self.marks)
        print(self.year)
    def stu_year(self):
        print(self.year)
stu_=student("Yash","A","Python",69,2026)
stu_.stu_det()
stu_.stu_year()

     ---------practice--------
class Animals:
    def __init__(self,animal,bread,color,gender):
        self.animal=animal
        self.bread=bread
        self.color=color
        self.gender=gender
    def animal_det(self):
        print(self.animal)
        print(self.bread)
        print(self.color)
        print(self.gender)


animal_1=Animals("Lion","Balayya","Yellow","Male")
animal_2=Animals("Tiger","NTR","Green ","Male")
animal_1.animal_det()
animal_2.animal_det()


-------
Encapsulation
-->        
'''





























