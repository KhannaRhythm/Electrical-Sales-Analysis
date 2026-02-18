CREATE TABLE IF NOT EXISTS public.sales_data
(
    sale_id integer,
    date date,
    product_name character varying(100) COLLATE pg_catalog."default",
    category character varying(50) COLLATE pg_catalog."default",
    quantity integer,
    selling_price numeric,
    total_sales numeric,
    purchase_price numeric,
    supplier character varying(150) COLLATE pg_catalog."default",
    profit numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sales_data
    OWNER to postgres;