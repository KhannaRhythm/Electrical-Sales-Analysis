/* Monthly Sales Trend */
SELECT 
    TO_CHAR(date, 'YYYY-MM') AS month,
    SUM(total_sales) AS monthly_sales
FROM sales_data
GROUP BY month
ORDER BY month;

/* High Sales but Low Profit */

SELECT 
    product_name,
    SUM(total_sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC, total_profit ASC;
/* These products sell a lot but margins are weak. Business should review supplier pricing or adjust selling price.*/


/* REORDER RECOMMENDATION */

SELECT 
    product_name,
    current_stock,
    reorder_level,
    recommended_reorder_qty
FROM inventory_data
WHERE recommended_reorder_qty > 0;
/* This ensures we never stock out high-demand products during supplier lead time. */


