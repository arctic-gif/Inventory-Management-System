# Importing necessary modules
import read  # module for reading data from txt file
import Write  # module for writing data to txt file
import Operation  # module for performing operations on data
import datetime  # module for working with dates and times
import random  # module for generating random numbers
read.heading()

# Function for user options
def userOptions():
    # Loop until the user chooses to exit
    loop = True
    while loop == True:
        # Displaying menu options
        print("Select Your Options To Continue")
        print("Press 1 To Sell To Customers: ")
        print("Press 2 For Purchase From Manufacturers: ")
        print("Press 3 For Exit: ")
        noloop = True
        # Loop until valid input is entered
        while noloop:
            try:
                takeninput = int(input("Enter any of the options to continue: \n"))
            except ValueError as e:
                # Displaying error message if input is not an integer
                print("You may only enter 1, 2 or 3 as an input!\n")
            else:
                noloop = False
        print("\n")
        if takeninput == 1:
            # Displaying the list of available laptops to the customer
            read.display()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            loop = True
            strloop = True
            # Loop until the customer's name is entered correctly
            while strloop:
                nameofcustomer = str(input("State your Name: \n").strip())
                try:
                    # Check if the name entered contains only alphabets
                    if nameofcustomer.replace(" ","").isalpha():
                        break
                    else:
                        raise ValueError("You may only enter alphabets!\n")
                except ValueError as f:
                    # Displaying error message if name entered contains non-alphabets
                    print(f"error:{f}")
                else:
                    strloop = False
            strloop2 = True
            # Loop until the customer's address is entered correctly
            while strloop2:
                customeraddress = str(input("State your Address: \n").strip())
                try:
                    # Check if the address entered contains only alphabets
                    if customeraddress.replace(" ", "").isalpha():
                        break
                    else:
                        raise ValueError("You may not enter non-alphabetical input\n")
                except ValueError as f:
                    # Displaying error message if address entered contains non-alphabets
                    print(f"error:{f}")
                else:
                    strloop2 = False
            noloop2 = True
            # Loop until the customer's contact number is entered correctly
            while noloop2:
                try:
                    contactno = int(input("Enter your Contact Number: \n"))
                except ValueError:
                    # Displaying error message if contact number contains alphabets
                    print("Contact Numbers dont have alphabets, Silly!\n")
                else:
                    noloop2 = False

            List = []
            while loop:
                validid = True
                dict = read.present_function()
                # Loop until a valid laptop ID is entered
                while validid:
                    enteredlaptopid = Operation.validation_num(dict)
                    # Display the quantity of the laptop in stock
                    print(f"We only have {dict[enteredlaptopid][3]} of the laptop in stock\n")
                    if int(dict[enteredlaptopid][3]) == 0:
                        # Ask the user if they want to select a different laptop
                        Operation.loop(validid)
                    else:
                        validid = False
                        # Get laptop quantity by validating the entered laptop id
                laptopquantity = Operation.validation_of_quantity(dict, enteredlaptopid, takeninput)
                # Update the dictionary for selling laptops
                dict = Operation.update_sell_laptops(enteredlaptopid, laptopquantity, List)
                # Update the .txt file
                Write.update_txtfile(dict)
                # Loop to ask the user if they want to buy more
                loop_1 = True
                while loop_1:
                    confirm = str(input("Do you want to keep buying?: (yes/no)\n").strip())
                    # If yes, break loop_1 and start again
                    if confirm == 'yes':
                        loop_1 = False
                        loop = True
                        # If no, break both loops
                    elif confirm == 'no':
                        loop_1 = False
                        loop = False
                    else:
                        # If inappropriate value, print error message
                        print("You may only enter either yes or no!\n")

            # Generate bill number and current date and time
            billnumber = random.randint(0, 500)
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            # Generate customer bill and update .txt file for selling
            Write.customer_bill_generate(nameofcustomer, customeraddress, contactno, List, billnumber, date, time)
            Write.bill_txt_sell(nameofcustomer, customeraddress, contactno, List, billnumber, date, time)
            print("\n")
            # Print thank you message
            print("Thank you for shopping with us.\n")
        # If user inputs 2
        elif takeninput == 2:
            # Display available laptops and get customer name
            read.display()
            print("------------------------------------------------------------------------------------------------------------------")
            strloop = True
            # Loop until the customer's name is entered correctly
            while strloop:
                nameofcustomer = str(input("State your Name: \n").strip())
                try:
                    # Check if the name entered contains only alphabets
                    if nameofcustomer.replace(" ", "").isalpha():
                        break
                    else:
                        raise ValueError("You may only enter alphabets!\n")
                except ValueError as f:
                    # Displaying error message if name entered contains non-alphabets
                    print(f"error:{f}")
                else:
                    strloop = False
            # Get dictionary of available laptops
            dict = read.present_function()
            # Initialize empty list
            List = []
            # Loop until customer decides to stop buying
            loop = True
            while loop == True:
                # Get laptop id and quantity
                enteredlaptopid = Operation.validation_num(dict)
                laptopquantity = Operation.validation_of_quantity(dict, enteredlaptopid, takeninput)
                # Update the dictionary for manufacturer purchase
                dict = Operation.update_manufacturer_purchase(enteredlaptopid, laptopquantity, List)
                Write.update_txtfile(dict)
                # Update the .txt file
                # Loop to ask the user if they want to buy more
                loop_1 = True
                while loop_1:
                    reinterrogate = str(input("Do you want to keep purchasing more laptops?: (yes/no)\n").strip())
                    # print("\n")
                    # If yes, break loop_1 and start again
                    if reinterrogate == 'yes':
                        loop_1 = False
                        loop = True
                    # If no, break both loops
                    elif reinterrogate == 'no':
                        loop_1 = False
                        loop = False
                    else:
                        # If inappropriate value, print error message
                        print("You may only enter eiter yes or no\n")
            # Generate bill number and current date and time
            billnumber = random.randint(0, 500)
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            # Generate manufacturer purchase bill and update .txt file
            Write.purchase_bill_generate(nameofcustomer, List, billnumber, date, time)
            Write.bill_txt_purchase(nameofcustomer, List, billnumber, date, time)
            print("\n")
            print("Thank you for shopping with us.\n")
        elif takeninput == 3:
            loop = False
            print("We appreciate you for giving us your valued time, we really hope you change your mind.\n")
            print("\n")
        else:
            print("The option you entered", takeninput, "is not valid.\n")
            print("\n")
    return takeninput


userOptions()