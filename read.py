def heading():
    '''this function shows the header part of gui'''
    # Displaying the header section of the GUI
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t  |WE WARMLY WELCOOME YOU TO!|")
    print("\t \t \t \t \t \t |Mato Electronics|")
    print("\n")
    print("\t \t \t \t \t   |Sangla , Kathmandu  | 987654431|")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

def present_function():
    """
    This function reads data from a file and returns a dictionary containing the laptop details.

    The file should have one line per laptop, with the laptop details separated by commas.

    The keys of the dictionary are auto-generated IDs, starting from 1 and incrementing by 1 for each laptop.
    """
    # Read data from file "laptops.txt" and store in dictionary
    dictionary = {}
    file = open("laptops.txt", "r")
    laptop_id = 1
    for line in file:
            line = line.strip() # remove newline character
            laptop_data = line.split(",") # split the line into laptop details
            dictionary[laptop_id] = laptop_data
            laptop_id += 1
    file.close()
    return dictionary

def display():
    a = 1
    """This function helps to show laptops details in a table."""
    # Displaying the laptop details in a tabular form
    text = open("laptops.txt", "r")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("{:<4}{:<20}{:<20}{:<8}{:<28}{:<20}{:<20}".format("SN", "Name", "Brand", "Price", "Quantity in stock", "Processor", "Graphics Card"))
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for value in text:
        print("{:<4}{:<20}{:<20}{:<8}{:<28}{:<20}{:<20}".format(a, *(value.strip().split(","))))
        a += 1
    text.close()

