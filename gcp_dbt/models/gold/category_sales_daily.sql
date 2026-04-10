-- models/gold/category_sales_daily.sql
{{ config(materialized='table') }}

SELECT
	order_date,
	category,
	SUM(total_amount) as daily_revenue,
	SUM(quantity) as items_sold
FROM {{ ref('stage_sales') }}
GROUP BY 1, 2

