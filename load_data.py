
import dataset
import csv
from datetime import datetime

s = 'sqlite:///data.db'
db = dataset.connect(s)

sales = db['sales']


with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    rows = [row for row in spamreader]
    for row in rows[1:]:
        d = {
            'week_sold': datetime.strptime(row[0], '%Y-%m-%d').date(),
            'price': float(row[1]),
            'num_sold': int(row[2]),
            'store_id': row[3],
            'product_code': row[4],
            'department_name': row[5]
        }
        print(d)
        sales.insert(d)
