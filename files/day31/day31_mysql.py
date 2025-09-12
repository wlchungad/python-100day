import mysql.connector

def safe_execute(cursor, sql_statement = ""): # just to avoid repeating a lot of try-except in following code
    try:
        if sql_statement[:4] == "SHOW":
            print (f"{sql_statement}:")
            cursor.execute(sql_statement)
            print (f"{sql_statement}:")
            for x in cursor:
                print (x)
        elif sql_statement[:6] == "SELECT":
            print (f"{sql_statement}:")
            cursor.execute("SELECT * FROM customers")
            myresult = cursor.fetchall()
            for x in myresult:
                print(x)
        else:
            cursor.execute(sql_statement)
    except Exception as e:
        print("Problem running %s: %s" % (sql_statement, e))
        exit(1)

if __name__ == "__main__":

    try:
        mysql_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@sssw0rd"
        )
    except:
        print("Mysql Connection failed")
        exit(1)

    # Create cursor per session
    # To keep connection like CLI, allow buffered=True
    cursor = mysql_db.cursor(buffered=True)
    # Create database
    safe_execute(cursor, "CREATE DATABASE IF NOT EXISTS mydatabase")
    # Show database
    safe_execute(cursor, "SHOW DATABASES")

    # for x in cursor:
    #     print(x)

    safe_execute(cursor, "USE mydatabase")
    sql = "DROP TABLE IF EXISTS customers"
    cursor.execute(sql)

    safe_execute(cursor, "CREATE TABLE IF NOT EXISTS " \
                            "customers (id INT AUTO_INCREMENT PRIMARY KEY, " \
                            "name VARCHAR(255)," \
                            "address VARCHAR(255))")
    # OR
    # safe_execute(cursor, "CREATE TABLE IF NOT EXISTS " \
    #                         "customers (name VARCHAR(255)," \
    #                         "address VARCHAR(255))")
    # safe_execute(cursor, "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    safe_execute(cursor, "SHOW TABLES")

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    cursor.execute(sql, val)
    mysql_db.commit()

    print(cursor.rowcount, "inserted.")

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
    ]

    cursor.executemany(sql, val)
    mysql_db.commit()

    print(cursor.rowcount, "inserted.")

    # read from table
    safe_execute(cursor, "SELECT * FROM customers")
    

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Michelle", "Blue Village")
    cursor.execute(sql, val)

    mysql_db.commit()

    print("1 record inserted, ID:", cursor.lastrowid)
    safe_execute(cursor, "SELECT * FROM customers")

    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = ("Valley 345", "Canyon 123")
    cursor.execute(sql, val)
    safe_execute(cursor, "SELECT * FROM customers")