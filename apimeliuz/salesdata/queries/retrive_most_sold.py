retrieve_query = """SELECT sale_date,product_id,product_title,product_image_url,store_name,store_id,sales_per_day 
FROM (SELECT *, MAX(total_sales_store) OVER (PARTITION BY product_id) as max_product_per_store, MAX(id) OVER (PARTITION BY product_id,store_id) as target_id
FROM (SELECT *, SUM(sales_per_day) OVER (PARTITION BY product_id,store_id) as total_sales_store
FROM salesdata_salesdata as sd
WHERE sd.product_id in (SELECT DISTINCT product_id FROM (SELECT DISTINCT product_id, SUM(sales_per_day) OVER (PARTITION BY product_id) as total_sales FROM salesdata_salesdata ORDER BY total_sales DESC) LIMIT 10)))
WHERE total_sales_store=max_product_per_store and id = target_id"""