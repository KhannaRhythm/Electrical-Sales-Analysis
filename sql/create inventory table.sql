CREATE TABLE IF NOT EXISTS public.inventory_data
(
    product_name character varying(100) COLLATE pg_catalog."default",
    current_stock integer,
    reorder_level integer,
    avg_daily_sales numeric,
    recommended_reorder_qty integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.inventory_data
    OWNER to postgres;