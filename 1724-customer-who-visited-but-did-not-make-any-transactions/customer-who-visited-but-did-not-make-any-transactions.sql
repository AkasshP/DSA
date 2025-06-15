# Write your MySQL query statement below
with counter as (select customer_id, v.visit_id from Visits v where v.visit_id not in (select visit_id from Transactions))
select customer_id, count(customer_id) as count_no_trans  from counter group by customer_id
