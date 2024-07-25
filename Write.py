import read


def update_txtfile(dict):
    # This function updates the text file with the dictionary values
    file = open("laptops.txt", "w")
    for i in dict.values():
        file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]))
        file.write("\n")
    file.close()


def customer_bill_generate(name, address, contactno, list, billnumber, date, time):
    global ship
    # This variable 'ship' stores whether the customer wants shipping or not
    ship_1 = True
    while ship_1:
        ship = input("Would you like the products to be shipped to your location?: (yes/no)\n")
        if ship.lower() == "yes":
            # If the customer wants shipping, set 'ship_cost' to 250
            ship_1 = False
            ship_cost = 250
        elif ship.lower() == "no":
            # If the customer doesn't want shipping, set 'ship_1' to False and skip shipping cost
            ship_1 = False
        else:
            print("Inappropriate value! Please enter yes or no.\n")

    read.heading()
    # Print the bill details
    print(f"\t\t\t\t\tBill no: {billnumber}")
    print(f"Date: {date}\t\t\t\t\t Time: {time}")
    print(f"Name of customer:  {name}")
    print(f"Address : {address}")
    print(f"Contact Number: {contactno}")
    t_total = 0

    # Print the details of each item in the customer's list
    for i in range(len(list)):
        c_name = list[i][1].replace(" ", "")
        print(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}")
        price1 = list[i][2].replace(" ", "")
        print(f"Price: {price1}\t\t\t Quantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        t_total = t_total + int(list[i][3])
        print(f"\n")

    # Calculate the total and grand total of the bill
    if ship == "yes":
        print(f"Shipping cost: {250}")
        print(f"Total: {t_total}")
        print(f"Grand total: {t_total + 250}")
    else:
        print(f"Total: {t_total}")


def bill_txt_sell(name,address,contactno,list,billnumber,date,time):
    # open a new file with the bill number as the filename
    file = open(f"{billnumber}.txt","w")

    # write customer information to the file
    file.write(f"/t/t/tBill no: {billnumber}\n")
    file.write(f"date: {date}\t\t\t\t\t Time: {time}\n")
    file.write(f"name:  {name}\n")
    file.write(f"Address: {address}\n")
    file.write(f"Number: {contactno}\n")

    # calculate the total price of all items and write each item to the file
    t_total=0
    for i in range(len(list)):
        c_name=list[i][1].replace(" ","")
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t Quantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        t_total=t_total+int(list[i][3])
        file.write(f"\n")

    # if shipping was requested, add the cost to the total price and write to the file
    if ship=="yes":
        file.write(f"Shipping cost: {250}\n")
        file.write(f"Total: {t_total}\n")
        file.write(f"Grand total: {t_total+250}\n")
    else:
        file.write(f"Total: {t_total}\n")

    # close the file
    file.close()


# Define a function to generate a purchase bill
# It takes name, list of items, bill number, date, and time as arguments
def purchase_bill_generate(name,list,billnumber,date,time):
    # Print the bill number, date, and time
    print(f"\t\t\t\t\tBill no: {billnumber}")
    print(f"Date: {date}\t\t\t\t\t Time: {time}")
    print("-------------------------------------------------------------------------")
    # Print the name of the customer
    print(f"Name:  {name}")
    t_total=0
    # Loop through the list of items
    for i in range(len(list)):
        # Replace any spaces in the company name with empty string
        c_name=list[i][1].replace(" ","")
        # Print the laptop name and company name
        print(f"Laptop Name: {list[i][0]}\t\tCompany Name: {c_name}")
        # Replace any spaces in the price with empty string and print the price and quantity
        price1 =list[i][2].replace(" ","")
        print(f"Price: {price1}\t\t \nQuantity: {list[i][4]}")
        # Print the total price of the item
        print(f"Total price: {list[i][3]}")
        # Calculate the total amount
        t_total=t_total+int(list[i][3])
        print(f"\n")
    # Calculate the VAT amount and print it
    print(f"Vat amount: {0.13*t_total}")
    # Calculate the grand total (total + VAT) and print it
    print(f"Grand Total :{(0.13*t_total) + t_total}")

# Define a function to generate a purchase bill text file
# It takes name, list of items, bill number, date, and time as arguments
def bill_txt_purchase(name,list,billnumber,date,time):
    # Create a new text file with the bill number as the file name
    file = open(f"{billnumber}.txt","w")
    # Write the bill number, date, and time to the file
    file.write(f"\\t\t\t\tBill no: {billnumber}\n")
    file.write(f"Date: {date}\t\t\t\t\t Time: {time}\n")
    # Write the name of the customer to the file
    file.write(f"Name:  {name}\n")
    t_total=0
    # Loop through the list of items
    for i in range(len(list)):
        # Replace any spaces in the company name with empty string
        c_name=list[i][1].replace(" ","")
        # Write the laptop name and company name to the file
        file.write(f"Laptop Name: {list[i][0]}\t\t\t\tCompany Name: {c_name}\n")
        # Replace any spaces in the price with empty string and write the price and quantity to the file
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t \nQuantity: {list[i][4]}\n")
        # Write the total price of the item to the file
        file.write(f"Total price: {list[i][3]}\n")
        # Calculate the total amount
        t_total=t_total+int(list[i][3])
        # Write a new line to the file
        file.write(f"\n")
    # Calculate the VAT amount and write it to the file
    file.write(f"Vat amount: {0.13*t_total}\n")
    file.write(f"Grand Total = {(0.13*t_total) + t_total}\n")