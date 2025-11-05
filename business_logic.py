import pprint
def decrease_stock(rawmaterials, raw_material_id, quantity):
    rawmaterials.loc[raw_material_id, 'CurrentStock'] -= quantity
    raw_material_name = rawmaterials.loc[raw_material_id, 'Description']
    if rawmaterials.loc[raw_material_id, 'CurrentStock'] < rawmaterials.loc[raw_material_id, 'Threshold']:
        print(f'{raw_material_name} falls below threshold.')
        print('Placing a purchase order to restock')
    else:
          print(f'{raw_material_name} stock reduced to {rawmaterials.loc[raw_material_id, 'CurrentStock']}')

def create_purchase_order(rawmaterials, raw_material_id, quantity):
    pass

def increase_stock(rawmaterials, raw_material_id, quantity):
    pass
def get_raw_material_id(raw_materials):
        raw_materials_ids = raw_materials.index.tolist()
        pprint.pprint(raw_materials)
        while True:
                print("Select a a raw material by its id: ")
                raw_material_id = input()
                if raw_material_id not in raw_materials_ids:
                        print("Invalid raw material id")
                else:
                        print(f"You selected {raw_material_id}")
                        break
        return raw_material_id
def rawmaterials_details(raw_materials, raw_material_id):
       return raw_materials.loc[raw_material_id]

def view_data(data_frame):
    print(data_frame)
    input("Press enter to continue...") 
