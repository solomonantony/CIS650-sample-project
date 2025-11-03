import os
import pandas as pd

def read_data():
    subfolder_path = "data"
    raw_materials = pd.read_json(os.path.join(subfolder_path, "raw_materials.json"))
    raw_materials.set_index('RawMaterialID', inplace=True)
    purchase_orders = pd.read_json(os.path.join(subfolder_path, "purchase_orders.json"))
    purchase_orders.set_index('PO_ID', inplace=True)
    vendors = pd.read_json(os.path.join(subfolder_path, "vendors.json"))
    vendors.set_index('VendorID', inplace=True)
    input("Press enter to continue...") 
    return vendors, raw_materials, purchase_orders
#