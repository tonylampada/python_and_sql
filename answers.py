import dataset 
# 1) There are 21 unique products in the store 
# 2) The total beverage sales in this store is $5277.5 in these three months. 
# Q1) Are these statements accurate? If not, what is the correct number? 
# Write a SQL query AND a python script to check the above.

s = 'sqlite:///data.db'
db = dataset.connect(s)

sql = 'select count(distinct product_code) as uniquecount from sales'
result = db.query(sql)
for row in result:
    print('There are %s unique products' % row['uniquecount'])

sql = '''
select store_id, sum(price * num_sold) as total_sales
from sales
group by store_id
'''

result = db.query(sql)
for row in result:
    print('store = %s, total_sales = %s' % (row['store_id'], row['total_sales']))

