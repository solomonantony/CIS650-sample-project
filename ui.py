"""
This is the user interface for the financial information system at 
We Build Stuff
"""
import pprint


def main():
        menu_text = """
        We Build Stuff FIS menu
        =======================
        1. Read data
        2. View Raw materials
        3. View purchase orders
        4. Reduce stock level
        5. Increase stock level
        6. Save changes
        7. Exit
        =======================

        """
        import pandas as pd
        import os
        import read_data, business_logic
        import utilities
        user_choice = 0
        while user_choice != 7:
                print(menu_text)
                user_choice = utilities.get_integer("Enter your choice ", 1, 7)
                if user_choice == 7:
                        if input("Are you sure? Y/N: ").upper() == "Y":
                                print("Goodbye")
                elif user_choice == 1:
                        print('Reading data...')
                        vendors, raw_materials, purchase_orders = read_data.read_data()
                elif user_choice == 2:
                        print('Viewing raw materials...')
                        business_logic.view_data(raw_materials)
                elif user_choice == 3:
                        print('Viewing purchase orders...')
                        business_logic.view_data(purchase_orders)
                elif user_choice == 4:
                        print('Reducing stock level...')
                        selected_raw_material_id = business_logic.get_raw_material_id(raw_materials)
                        details = business_logic.rawmaterials_details(raw_materials, selected_raw_material_id)
                        pprint.pprint(details)
                        reduce_by = utilities.get_integer("Enter the quantity to reduce:",0, details['CurrentStock'])
                        print(f"Reducing by {reduce_by}")
                        business_logic.decrease_stock(raw_materials, selected_raw_material_id, reduce_by)
                        pprint.pprint(raw_materials.loc[selected_raw_material_id])
                        input("Press enter to continue...") 
                elif user_choice == 5:
                        print('Increasing stock level...')
                else:
                        print("under development")

if __name__ == "__main__":
    main()


    
