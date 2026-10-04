-- Write your query below
select name from customers
where name not in (select c.name from customers c join orders o on o.customer_id=c.id)