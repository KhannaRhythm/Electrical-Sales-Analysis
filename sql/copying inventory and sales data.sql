COPY inventory_data
FROM '"C:\Users\HP\Desktop\Ankur-lights-and-electricals-sales-analysis\data\cleaned_inventory.csv"'
DELIMITER ','
CSV HEADER;

COPY sales_data
FROM '"C:\Users\HP\Desktop\Ankur-lights-and-electricals-sales-analysis\data\cleaned_inventory.csv"'
DELIMITER ','
CSV HEADER;
