import sqlite3

# define connection and cursor
# connection: represents the database
# cursor: used to interact with the database

connection = sqlite3.connect('store_transactions.db')

cursor = connection.cursor()

# create stores table

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

# create purchases table

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, 
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add to purchases

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")