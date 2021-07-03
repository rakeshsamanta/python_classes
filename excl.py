import csv
from os import write
data = [('smith, bob', 2), ('carol', 3), ('ted', 4), ('alice', 5)]

with open('hero.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['name', 'num'])
    for row in data:
        csv_out.writerow(row)