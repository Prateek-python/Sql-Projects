import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="7877",
    database="sql2"
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE sql2")
# ...................................................
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
# .....................................................
# mycursor.execute("CREATE TABLE customers ( name VARCHAR(255),address VARCHAR(255))")
# .....................................................
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
# ........................................................
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# ....................................
# sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
# val=("John","Highway 21")
# val1=("RAM","Hjndhwg")
# val2=("Yohn","qwqwqw")
# val3=("Oohn","iswuyg")
# many_values = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.execute(sql,val)
# mycursor.execute(sql,val1)
# mycursor.execute(sql,val2)
# mycursor.execute(sql,val3)
# mycursor.executemany(sql,many_values)
# mydb.commit()
# .......................
# mycursor.execute("SELECT * FROM customers")
# myresult=mycursor.fetchone()
# for x in myresult:
#     print(x)
# .............................
# mycursor.execute("SELECT * FROM customers ORDER BY name DESC")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)