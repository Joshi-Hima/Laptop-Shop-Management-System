#defining a function to get the data from the laptop file
def read_frpm_laptop():
    '''Iterates through the laptop file from line to line and gets the data'''
    file=open("laptop.txt","r")
    laptop_dict ={}
    lap_id=1
    for line in file:
        line = line.replace("\n","")  #replaces new line with space
        l= line.split(",")  #splits when finds commas
        laptop_dict[lap_id]=l
        lap_id+= 1
    file.close()
    return laptop_dict

#defining a function to replace the commas with space
def rep_with_space():
    '''Replacescommas with space by iterating to the file'''
    file = open("laptop.txt", "r")
    a = 0
    for line in file:
        print(a+1, "\t\t" + line.replace(",", "\t\t"))   #replaces line with tabs
        a = a + 1
        if(a == 5):
            break
    file.close()
