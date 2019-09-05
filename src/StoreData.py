import mysql.connector

def StoreData(product):
    con =  mysql.connector.connect(host="localhost", user="tester", passwd="password", database="steam", port= 3306)
    print("Connected to mysql")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products(name varchar(255),price varchar(10),PRIMARY KEY (name));")
    x = 0
    while (x < len(product.name)):
        cur.execute("REPLACE INTO products(name, price) VALUES (%s,%s);",(product.name[x], product.price[x]))
        x+= 1
    print("Data Inserted")
    con.commit()
    con.close()
