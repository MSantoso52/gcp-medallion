-- models/silver/stage_sales.sql
{{ config(materialized='table') }}

SELECT
  order_id,
  CAST(order_date AS DATE) as order_date,
  LOWER(category) as category,
  product_name,
  quantity,
  unit_price,
  (quantity * unit_price) as total_amount,
  COALESCE(email, 'unknown@example.com') as customer_email
FROM {{ source('bronze_layer', 'raw_sales') }}
WHERE order_id IS NOT NULL

