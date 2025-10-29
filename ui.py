"""
This is the user interface for the financial information system at 
We Build Stuff
"""
menu_text = """
   We Build Stuff FIS menu
   =======================
   1. Read data
   2. View Raw materials
   3. View purchase orders
   4. Reduce stock level
   5. Increase stock level
   6. Exit
   =======================

"""
import pandas as pd
import os
import view_data, read_data

while True:
    print(menu_text)
    user_choice = int(input("Enter your choice [1-6]"))
    if user_choice == 6:
        if input("Are you sure? Y/N: ").upper() == "Y":
            print("Goodbye")
            break
    elif user_choice == 1:
            print('Reading data...')
            vendors, raw_materials, purchase_orders = read_data.read_data()
    elif user_choice == 2:
            print('Viewing raw materials...')
            view_data.view_data(raw_materials)
    elif user_choice == 3:
            print('Viewing purchase orders...')
            view_data.view_data(purchase_orders)
    else:
            print("under development")

    
