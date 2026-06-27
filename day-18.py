class Hotel:
    def Non_veg(self):
        print("Mutton_biryanni")
        print("Chicken_biryanni")
    def veg(self):
        
        print("veg_friedrice")

    
    def Menu(self):
        print("\n1.Non_veg items \n2.Veg_items")
        user_choice=int(input("Enter Your Option: "))
        if user_choice == 1:
            self.Non_veg()
            
        elif user_choice==2:
            self.veg()
            
ho=Hotel()
ho.Menu()
        
      
'''
Value
zero division
index
type
file not found
name  
'''
    
