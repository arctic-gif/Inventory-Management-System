import read  # Importing a module named read

def update_sell_laptops(laptopid, quantityoflaptop, List):
    """This function updates the inventory when a laptop is sold.

    laptop_id -- the ID of the laptop being sold
    quantity -- the number of laptops being sold
    inventory -- a dictionary containing laptop IDs as keys and laptop details as values"""

    file = read.present_function()  # Reading data from file using the present_function() function from the read module
    for a in file.keys():  # Looping through the keys in the file dictionary
        if laptopid == a:  # Checking if the laptop id is present in the dictionary
            quantity = int(file[laptopid][3])  # Extracting the quantity of the laptop from the dictionary
            if quantityoflaptop <= quantity:  # Checking if the quantity of the laptop is greater than or equal to the requested quantity
                file[laptopid][3] = str(quantity - quantityoflaptop)  # Subtracting the requested quantity from the quantity of the laptop in the dictionary
                price = quantityoflaptop * int(file[laptopid][2].replace("$", ""))  # Calculating the total price of the requested quantity of laptops
                List.append([file[laptopid][0], file[laptopid][1], file[laptopid][2], price, quantityoflaptop])  # Appending the laptop details to the List
    return file  # Returning the updated file dictionary

def update_manufacturer_purchase(laptopid, quantityoflaptop, List):
    """This function updates the inventory when a laptop is purchased from the manufacturer."""

    file = read.present_function()  # Reading data from file using the present_function() function from the read module
    for a in file.keys():  # Looping through the keys in the file dictionary
        if laptopid == a:  # Checking if the laptopid is present in the dictionary
            quantity = int(file[laptopid][3])  # Extracting the quantity of the laptop from the dictionary
            file[laptopid][3] = str(quantity + quantityoflaptop)  # Adding the purchased quantity to the quantity of the laptop in the dictionary
            price = quantityoflaptop * int(file[laptopid][2].replace("$", ""))  # Calculating the total price of the purchased quantity of laptops
            List.append([file[laptopid][0], file[laptopid][1], file[laptopid][2], price, quantityoflaptop])  # Appending the laptop details to the List
    return file  # Returning the updated file dictionary

def validation_num(dict):
    """This function checks validation of laptop id input by user"""
    validation_loop = True
    vvalues = list(dict.keys())  # Converting the keys of the dictionary into a list
    pause = vvalues[-1]  # Extracting the last element from the list
    while validation_loop:
        try:
            laptopid = int(input("Enter the ID of the laptop you wish to buy: \n"))  # Asking the user for the laptop ID
        except ValueError as num:
            print("Please enter an integer value!\n")  # Printing an error message if the user enters a non-integer value
        else:
            if laptopid <= 0:
                print("Please enter a valid Laptop ID!\n")  # Printing an error message if the user enters a negative or zero ID
            elif 0 <= laptopid <= pause:
                if laptopid in vvalues:
                    validation_loop = False  # Ending the validation loop if the ID is valid
            else:
                print("The input you have entered is invalid, please enter a valid input.\n")  # Printing an error message if the user enters an ID that is not present

    return laptopid

def validation_of_quantity(dict, laptopid, takeninput):
    """This function checks the validation of the quantity of laptops to be purchased"""
    word_loop = True
    while word_loop:
        try:
            laptop_quantity = int(input("Enter the quantity of laptops you want to purchase: \n"))
        except ValueError as a:  # If the user enters a non-integer value, catch the exception
            print("Please enter an integer value.\n")
        else:
            if laptop_quantity <= 0:
                print("You may not enter negative values\n")
                word_loop = True
            else:
                word_loop = False
                quantity_available = int(dict[laptopid][3])  # Retrieve the available quantity of laptops from the dictionary
                print("There are now " + str(quantity_available + laptop_quantity) + " laptops available.\n")
                if takeninput == 1:  # If the input is for purchasing laptops
                    if quantity_available >= laptop_quantity:  # Check if the available quantity is enough
                        word_loop = False  # If it is enough, exit the loop
                    else:
                        print("There are only " + str(quantity_available) + " laptops available.\n")
                elif takeninput == 2:  # If the input is for updating the stock
                    if laptop_quantity <= 0:  # Check if the input quantity is valid
                        print("Sorry, the stock cannot be updated with this quantity.\n")  # Inform the user if it is not
                    else:
                        word_loop = False  # Otherwise, exit the loop
    return laptop_quantity  # Return the validated quantity of laptops

def loop(loop):
    """This function asks the user if they want to buy again and updates the loop flag accordingly."""
    loop_1 = True
    while loop_1:
        ask_again = str(input("Do you want to buy again?: (yes/no)").strip())
        if ask_again.lower() == 'yes':
            loop_1 = False
            loop = True
        elif ask_again.lower() == 'no':
            loop_1 = False
            loop = False
        else:
            print("You have entered an invalid value, please enter a valid value\n")
    return loop
