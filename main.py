from datetime import datetime
from read import *
from operations import *
from write import *

print("--------------------------------------------------------------------")
print("/t/t/t/t Welcome Dhangadhi Laptop Store")
print("--------------------------------------------------------------------")

por = read_frpm_laptop()
loop = True

while loop == True:
    print("Please enter  1 to sale the laptop to costumer:")
    print("Please enter  2 to purchase the laptop from manufracturer:")
    print("Please enter 3 to exit from the system:")
    print("\n")
    opt = True
    while opt == True:
        try:
            user_inp = int(input("Please choose one option: ") )  #tring this line of code
            opt=False
        except:
            print("Invalid value provided. Please choose correct value.")  #print statement in except
    print("\n")
    if user_inp == 1:
        sell_to_cus(por)  #calling a function from operations
    elif user_inp == 2:
        buy_from_manu(por)  #calling a function from operations
    elif user_inp == 3:
        loop == False
        print("Thank you for visiting our shop.")
        break
    else:
        print("The input you provided does not match the option. Please provide correct option to choose.")
    print("\n")

        









            
            
