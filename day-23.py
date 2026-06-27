

'''
Matplotlib:
-->This provides various plots and customization options to make any visualization and meaninful
Basic structure
--------------------
1.Axis - (x,y)
2.Title - (Title)

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
plt.plot(x,y)
plt.title("line plot")
plt.show()


Line Plot :
This is use to display data points connected by straight lines 



import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[10,20,15,12,17,19]
plt.xlabel("overs")
plt.ylabel("score")
plt.plot(x,y)
plt.title("R.C.B Score")
plt.show()


import matplotlib.pyplot as plt
marks=[10,20,15]
stu=["Ganesh","Yashwanth","Anish"]
plt.bar(stu,marks,color='green')
plt.ylabel("students")
plt.xlabel("Marks")
plt.title("Student Marks")
plt.show()



import matplotlib.pyplot as plt
sales=[2000,2300,2500,2700]
year=[2017,2018,2019,2020]
plt.bar(year,sales,color='red')
plt.ylabel("Year")
plt.xlabel("Sales")
plt.title("BMW sales")
plt.show()



import matplotlib.pyplot as plt
sales=[2000,2300,2500,2700]
year=[2017,2018,2019,2020]
plt.pie(year,labels=sales)
plt.title("BMW sales")
plt.legend(year)
plt.show()

'''

 
import matplotlib.pyplot as plt
sales=[2000,2300,2500,2700]
year=[2017,2018,2019,2020]
plt.scatter(year,labels=sales)
plt.ylabel("no. ")
plt.title("BMW sales")
plt.show()












