def sell_prod(name, ph_no, date_time, pur_laptops,total, ship_price, grand_tot):
            '''This function is used for printing the bills on the screen'''
    
            print("\n")
            print("------------------------------------------------------------------------")
            print("\t Welcome to Dhangadhi Laptop Store")
            print("\t Dhangadhi, Kailali | Contact no: 0123456789")
            print("\n")
            print("------------------------------------------------------------------------")
            print("Your details are given below:")
            print("------------------------------------------------------------------------")
            print("Your name:"+str(name))
            print("Your contact number: "+str(ph_no))
            print("\n Your date and time of purchase: "+str(date_time))
            print("\n")
            print("Product \t\t\t Quantity \t\t Per item price \t\t\t Total price")
            print("\n")
            for i in pur_laptops:
                print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
            print("-")
            print("Your total amount is : $"+str (total))
            print("Your total Shipping charge is : $", ship_price)
            print("Your fina grand total is : $"+ str(grand_tot))
            print("\n")

def sell_prod_bill(name,ph_no,date_time, pur_laptops, total,ship_price, grand_tot):
        '''This function is used for wiritingthe bill in the file'''
        file= open(str(name)+".txt", "w")  #generates a unique file
        file.write("\n")
        file.write("\n------------------------------------------------------------------------")
        file.write("\n Welcome to Dhangadhi Laptop Store")
        file.write("\n------------------------------------------------------------------------")
        file.write("\n kamalpokhari kathmandu|phone no:7585858")
        file.write("\n")
        file.write("\n------------------------------------------------------------------------")
        file.write("\n Customer  details are:")
        file.write("\n")
        file.write("\n------------------------------------------------------------------------")
        file.write("\nName of the costumer:"+str(name))
        file.write("\n")
        file.write("\nContact number: "+str(ph_no))
        file.write("\n")
        file.write("\n Date and time of purchase: "+str(date_time))
        file.write("\n")
        file.write("Product \t\t\t Quantity \t\t Unit price \t\t\t Total Price\n")
        file.write("\n")

        for i in pur_laptops:
             
            file.write(str(i[0])+"\t\t\t "+str(i[1])+" \t\t "+str(i[2])+" \t\t\t "+"$"+str(i[3]) )


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("\nYour Shipping charge is : $ " +""+ str(ship_price) +"\n")
        file.write("\nGrand Total : $" + str(grand_tot))
        file.write("\n")
        file.close()

def buy_from_manu(name, ph_no, date_time, pur_laptops, total, vat_amt, grand_tot):
        '''This function is used to print bills on the screen that the user bought from the manufacturer'''
        print("\n")
        print("\t \t \t \t \t \t \t Welcome to Dhangadhi Laptop Store")
        print("\n")
        print("\n\t \t \t \t \t Dhangadhi, Kailali | Phone no: 9865818171")
        print("\n")
        print("\n-------------------------------------------- ")
        print("Product details: \n")
        print("\n-----------------------------------------------------")
        print("\nYour Name: "+ str(name))
        print("\nYour contact number: "+ str(ph_no))
        print("\nYour date and time of purchase: "+ str(date_time))
        print("-")
        print("\n")
        print("Your purchase Details are: ")
        print("-")
        print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        print("-")
        for i in pur_laptops:
            print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
        print("-")
        print("Your total is : $"+str (total))
        print("Your vat amount is : $", vat_amt)
        print("Your final price with grand total : $"+ str(grand_tot))
        print("\n")

def buy_from_manu_bill(name, ph_no, date_time, pur_laptops, total, vat_amt, grand_tot):
        '''This function is used to writes the bills by generating a unique file'''
        file= open(str(name)+ "file.txt", "w")
        file.write("\n")
        file.write("\t \t \t \t \t \t \t Welcome to Dhangadhi Laptop Store")
        file.write("\n")
        file.write("\t \t \t \t \t DHangadhi, Kailali | Phone no: 9865818171")
        file.write("\n" )
        file.write("\nYour Name: " + str(name))
        file.write("\nYour contact number: " + str(ph_no))
        file.write("\nYour date and time of purchase: " + str(date_time))
        file.write("\n" )
        file.write("\n")
        file.write("Ypur purchase Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in pur_laptops:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("\nYour Shipping charge is : $ " +""+ str(vat_amt) +"\n")
        file.write("\nYour final price with grand Total : $" + str(grand_tot))
        file.write("\n")
        file.close()

