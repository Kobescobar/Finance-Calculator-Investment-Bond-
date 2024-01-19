 
# Importing the math function 
import math

Highlight = """
Investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu below to proceed: 
"""

print(Highlight)



# creating the menu for user input 
while True: 
     user_choice = ["investment", "bond"]
     menu = input("Please enter either investment or bond: ").lower()
     if menu in user_choice:
        print(f"You have selected {menu}: ")
        break
     else: 
         print("You have made an invalid selection, Please try again.")

   


#  categorizing user input to investment
if menu == "investment": 
    while True:
        try:  
         p = float(input("Please enter the amount you would like to invest: "))      
         p = round(p) 
         r = float(input("Please enter the interest rate (exclude the percentage symbol): "))   
         r1 = r/100 
         t = float(input("Please enter the number of years you plan to invest: "))
         t = round(t)
         break

        except ValueError:
            print(" You have entered a wrong input. Please try again ")
              

    while True: 
            interest = input("Please select simple or compound interest: ").lower()
            interest_choice = ["simple", "compound"]
            print(f"You have selected {interest}")
            if interest in interest_choice:
                break
            else: 
                print("You have made an invalid selection. Please try again. ")
                     
                     
    if interest == "simple":
            A = p * (1 + r1 * t)        
            A = round(A)
            print(A)
            print(f"You will get back {A}, for {t} year(s) investment at {r}% interest rate. ")

    elif interest == "compound":
        B = p * math.pow((1+r1), t)
        B = round(B)
        print(B)
        print(f"You will get back {B}, for {t} years(s) investment at {r}% interest rate. ")
                      

# categorizing user input for bond
elif menu == "bond":
 while True: 
     try: 

# getting user input for bond and creating varibales for each detail
      p = float(input("Please enter the present value of the house: "))
      i = float(input("Please enter the monthly interest rate, leaving out the perecentage symbol: "))
      i = i/100 # Convering user interest rate input to percentage
      i = 1/12 # converting user interest rate input to by monthly 
      n = float(input("Please enter the number of months it will take to repay the bond: "))
      n = round(n)
      break

     except ValueError:
      print("You have made an invalid selection, please try again")

# calculating repayment 
 repayment = (i * p)/(1-(1+i)**(-n))
 repayment = round(repayment, 3)
 print(repayment)
 print(f"You will pay {repayment}, every month for {n} months to repay the bond")

 



     
