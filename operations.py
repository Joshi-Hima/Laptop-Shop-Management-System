from datetime import datetime
from read import *
from write import *
from main import *

def sell_to_cus(por):
        '''This functions basically runs the operation when the user wants to buy laptops from customer'''
        wanna_buy_more = True

        name = input("Please provide your name: ") #takes the name of user
        print("\n")

        while wanna_buy_more == True:
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t \tLaptop Names \t\tCompany  \t\t price \t\tQuantity   \tProcessor\t\t Graphics")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")

            rep_with_space()   #calling the function from read file

            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------" )
        
            print("\n")
            #applying loop 
            sold = False
            while sold == False:
                try:
                    laptop_id = int(input("Provide the ID of laptop you want to buy: "))
                    
                

                #checking if the ID provided by user is valid or not
                    while laptop_id <= 0 or laptop_id > len(por):
                        print("The laptop ID you provided is incorrect. Please provide the correct ID")
                        print("\n")

                        try:
                            laptop_id = int(input("Provide the ID of laptop you want to buy: "))
                        except:
                            print("No string value allowed. Please provide integer values in the place of ID")
                    sold = True
                
                except:
                    print("No string value allowed. Please provide integer values in the place of ID")
           
            print("\n")
            
            ph_no = input("Provide your phone number: ")  #takes phone number from the user
            print("\n")
            sold = False
            while sold == False:   #applying loop 
                try:
                    cus_qty = int(input("Provide the quantity of laptop you want to buy: "))    
                    print("\n")
                    #checking for the valid quantity
                    quantity= por[laptop_id][3]
                    if cus_qty <= 0 or cus_qty > int(quantity):
                        print("Dear user, the quantity you are looking foe is not available.")
                        print("\n")
                        qty= int(input("Provide the quantity laptops you want to buy: "))
                    print("\n")  
                   
                except:
                    print("No string value allowed. Please provide integer values in the place of ID")  
            
            #storing the information in the text file
                sold=True
            file =open("laptop_details.txt","w")
            por[laptop_id ][3]= int(por[laptop_id][3])-int(cus_qty)
            for values in por.values():
                file.write(str(values[0])+","+str(values[2])+","+str(values[3]))  #writes the values in the file in the respective index
                file.write("\n")
            file.close()
            
            #storing the details in variables
            lap_name = por[laptop_id][0]
            qty_of_laptop = cus_qty
            per_price = por[laptop_id][2]
            price_of_selected_laptop_qty = por[laptop_id][2].replace("$", '')
            tot_Price = int(price_of_selected_laptop_qty) * int(qty_of_laptop)
            gr_card = por[laptop_id][5]

            #list is created to store the details of the items that user bought
            pur_laptops = []
            pur_laptops.append([lap_name, qty_of_laptop, per_price, tot_Price, gr_card])

            wanna_purchase_more = input("Dear user, do you want to buy more items? (Y/N)").upper()
            print("\n")
        
            if wanna_purchase_more == "Y":
                wanna_buy_more = True
            else:
                wanna_buy_more=False
                total = 0
                ship_price = 150
                
            for i in pur_laptops:

                #dding the shipping price as 150 and adding the price in grand total  
                total += int(i[3])
                ship_price= 150
                grand_tot = total + ship_price
            date_time = datetime.now()   #printing the current date and time  of the purchase

            #calling the functions from write file
            sell_prod(name, ph_no, date_time, pur_laptops,total, ship_price, grand_tot)
            sell_prod_bill(name,ph_no,date_time, pur_laptops, total,ship_price, grand_tot)


def buy_from_manu(por):
        '''This function basically runs the operations when the owner wants to purchase laptops from manufacturer'''
        pur_laptops = []
        wanna_buy_more = True

        while wanna_buy_more== True:
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t \tlaptop name \t\tcompany name \t\t price \t\tquantity   \tProcessor\t\t Graphics")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")

            file = open("laptop.txt", "r")  #opening the txt file
            a = 1
            for line in file:
                print(a, "\t\t" + line.replace(",", "\t\t"))   #replacing commas with tabs
                a = a + 1
            print("----------------------------------------------------------------------------------------------------------------------------------------" )
            file.close()
            print("\n")
            sold = False
            while sold == False:
                try:
                    laptop_id = int(input("Provide the ID of laptop you want to buy: "))
                    
                    #checking the ID of laptop provided is cirrect or not
                    while laptop_id <= 0 or laptop_id > len(por):
                        print("Please provide valid laptop ID!")
                        print("\n")

                        try:
                            laptop_id = int(input("Provide the ID of laptop you want to buy: "))  #trying this code
                        except:
                            print("No string value allowed. Please provide integer values in the place of ID")



                    sold = True    #assigning sold as true
                
                except:
                    print("Please enter the required integer values")
            
            print("\n")
            name = "Dhangadhi Laptop Store"
            print("\n")
            
            ph_no = 9865818171
            print("\n")

            sold = False
            while sold == False:    #applying loop
                try:
                    cus_qty = int(input("Provide the quantity of laptop you want to buy: "))    
                    print("\n")
                    
                    #checking laptop quantuty 
                    qty= por[laptop_id][3]
                    if cus_qty <= 0 or cus_qty > int(qty):
                        print("Dear user, the quantity you've asked for is not available right now.")
                        print("\n")
                        qty= int(input("Provide the quantity laptops you want to buy: "))
                    print("\n")
                    
                    sold= True
                except:
                    print("No string value allowed. Please provide integer values in the place of ID")   #printing statement in except 
            por[laptop_id][3]= int(por[laptop_id][3])+int(cus_qty)
            
            #storing it in a next file  
            file =open("laptop_details.txt","w")  
            for values in por.values():
                file.write(str(values[0])+","+str(values[2])+","+str(values[3]))
                file.write("\n")
            file.close()
            por[laptop_id][3] = int(por[laptop_id][3]) + int(laptop_id)

            laptop_name = por[laptop_id][0]
            qty_of_laptop = cus_qty
            per_price = por[laptop_id][2]
            price_of_selected_laptop_qty = por[laptop_id][2].replace("$", '')
            tot_price = int(price_of_selected_laptop_qty) * int(qty_of_laptop)
            gr_card = por[laptop_id][5]

            #adding the datas in the list
            pur_laptops.append([laptop_name, qty_of_laptop, per_price, tot_price, gr_card])

            #asking user if they want to buy more items or not
            wanna_pur_more = input("Dear user, do you want to buy more items? (Y/N) ").upper()
            print("\n")
        
            if wanna_pur_more == "Y":
                wanna_buy_more = True
            else:
                wanna_buy_more=False
                total = 0
                vat_per = float(0.13)  #adding 13% as the VAT amount 
                
                for i in pur_laptops:
                    total += int(i[3])
                vat_amt = float(vat_per )*int(total)
                grand_tot = total + vat_amt
                date_time = datetime.now()
                
                buy_from_manu(name, ph_no, date_time, pur_laptops, total, vat_amt, grand_tot)


                buy_from_manu_bill(name, ph_no, date_time, pur_laptops, total, vat_amt, grand_tot)
