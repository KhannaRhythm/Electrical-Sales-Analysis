import pandas as pd
import os

# -----------------------------
# PATH SETUP (IMPORTANT)
# -----------------------------

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data")

sales_file = os.path.join(data_path, "sales_data.xlsx")
purchase_file = os.path.join(data_path, "purchase_data.xlsx")
inventory_file = os.path.join(data_path, "inventory_data.xlsx")

# -----------------------------
# LOAD DATA
# -----------------------------

sales = pd.read_excel(sales_file)
purchase = pd.read_excel(purchase_file)
inventory = pd.read_excel(inventory_file)

print("Files loaded successfully")

# -----------------------------
# DATA CLEANING
# -----------------------------

# Force convert date column
sales['date'] = pd.to_datetime(sales['date'], errors='coerce')

# Check for conversion errors
if sales['date'].isnull().any():
    print("Warning: Some dates could not be converted.")

# Convert to string format required by PostgreSQL
sales['date'] = sales['date'].dt.strftime('%Y-%m-%d')

print("Date format after conversion:")
print(sales['date'].head())


# Total Sales
sales['total_sales'] = sales['quantity'] * sales['selling_price']

# Merge purchase price
merged = sales.merge(purchase, on='product_name', how='left')

# Profit calculation
merged['profit'] = (
    merged['selling_price'] - merged['purchase_price']
) * merged['quantity']

# -----------------------------
# REORDER RECOMMENDATION
# -----------------------------

avg_daily_sales = (
    merged.groupby('product_name')['quantity']
    .mean()
    .reset_index(name='avg_daily_sales')
)

inventory = inventory.merge(avg_daily_sales, on='product_name', how='left')
inventory['avg_daily_sales'] = inventory['avg_daily_sales'].fillna(0)

LEAD_TIME_DAYS = 7

inventory['recommended_reorder_qty'] = (
    inventory['avg_daily_sales'] * LEAD_TIME_DAYS
) - inventory['current_stock']

inventory['recommended_reorder_qty'] = inventory['recommended_reorder_qty'].apply(
    lambda x: max(0, round(x))
)

# -----------------------------
# SAVE CLEANED FILES
# -----------------------------

merged.to_csv(os.path.join(data_path, "cleaned_sales.csv"), index=False)
inventory.to_csv(os.path.join(data_path, "cleaned_inventory.csv"), index=False)

print("Data processing completed successfully")
