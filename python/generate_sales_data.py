import os
import pandas as pd
from datetime import datetime, timedelta
import random

products = [
    ("LED Bulb 9W", "LED Lights", 120),
    ("LED Bulb 12W", "LED Lights", 160),
    ("Tube Light 20W", "Tube Lights", 350),
    ("Switch Board", "Switches", 220),
    ("Ceiling Fan", "Fans", 2200),
    ("Wire 1.5 sq mm", "Wires", 95),
    ("Extension Board", "Accessories", 450)
]

rows = []
start_date = datetime(2024, 10, 1)

sale_id = 1
for i in range(60):
    product = random.choice(products)
    date = start_date + timedelta(days=i)
    quantity = random.randint(2, 18)

    rows.append([
        sale_id,
        date.strftime("%Y-%m-%d"),
        product[0],
        product[1],
        quantity,
        product[2]
    ])
    sale_id += 1

df = pd.DataFrame(rows, columns=[
    "sale_id", "date", "product_name", "category", "quantity", "selling_price"
])
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(project_root, "data")
os.makedirs(data_path, exist_ok=True)

file_path = os.path.join(data_path, "sales_data.xlsx")

df.to_excel(file_path, index=False)

print("Sales data generated successfully")




# Generate Purchase Data

suppliers = [
    "Philips Distributor",
    "Havells Supplier",
    "Local Electrical Wholesale",
    "Surya Electricals",
    "Anchor Supply Co."
]

purchase_rows = []

for product in products:
    product_name = product[0]
    selling_price = product[2]
    
    # Purchase price = 60% to 85% of selling price (realistic margin)
    purchase_price = round(selling_price * random.uniform(0.6, 0.85), 2)
    
    supplier = random.choice(suppliers)

    purchase_rows.append([
        product_name,
        purchase_price,
        supplier
    ])

purchase_df = pd.DataFrame(purchase_rows, columns=[
    "product_name",
    "purchase_price",
    "supplier"
])

purchase_file_path = os.path.join(data_path, "purchase_data.xlsx")

purchase_df.to_excel(purchase_file_path, index=False)

print("Purchase data generated successfully")




# Generate Inventory Data



inventory_rows = []

for product in products:
    product_name = product[0]
    
    # Random realistic stock between 20 and 150
    current_stock = random.randint(20, 150)
    
    # Reorder level = minimum stock required
    reorder_level = random.randint(30, 60)

    inventory_rows.append([
        product_name,
        current_stock,
        reorder_level
    ])

inventory_df = pd.DataFrame(inventory_rows, columns=[
    "product_name",
    "current_stock",
    "reorder_level"
])

inventory_file_path = os.path.join(data_path, "inventory_data.xlsx")

inventory_df.to_excel(inventory_file_path, index=False)

print("Inventory data generated successfully")

