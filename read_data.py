import os
import pandas as pd

def read_data():
    subfolder_path = "data"
    raw_materials = pd.read_json(os.path.join(subfolder_path, "raw_materials.json"))
    purchase_orders = pd.read_json(os.path.join(subfolder_path, "purchase_orders.json"))
    vendors = pd.read_json(os.path.join(subfolder_path, "vendors.json"))
    input("Press enter to continue...") 
    return vendors, raw_materials, purchase_orders
#