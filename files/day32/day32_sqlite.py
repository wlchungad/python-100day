import sqlite3

# conn = sqlite3.connect('test.db') # This creates a test.db in current directory
# OR
conn = sqlite3.connect(':memory:') # creates a RAM-only instance, i.e., deleted upon completion
cursor = conn.cursor()
cursor.execute('''DROP TABLE IF EXISTS STUDENTS''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENTS(
        ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    NOT NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        TUTORION_FEE    REAL,
        RESULT          INT
    );
    ''')
conn.commit()

cursor.execute('''
    INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,TUTORION_FEE,RESULT) \
    VALUES (1, 'Paul', 32, 'House 1', 20000.00 , 50)
    ''')
cursor.execute('''
    INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,TUTORION_FEE,RESULT) \
    VALUES (2, 'Peter', 20, 'House 3', 20000.00 , 60)
    ''')
cursor.execute('''
    INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,TUTORION_FEE,RESULT) \
    VALUES (3, 'Ann', 24, 'House 5', 20000.00 , 90)
    ''')
cursor.execute('''
    INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,TUTORION_FEE,RESULT) \
    VALUES (4, 'Anna', 40, 'House 9', 42100.00 , 70)
    ''')
cursor.execute('''
    INSERT INTO STUDENTS (ID,NAME,AGE,ADDRESS,TUTORION_FEE,RESULT) \
    VALUES (5, 'Jane', 90, 'House 2', 0.00,  30)
    ''')
conn.commit()

read_cursor = cursor.execute("SELECT ID,NAME,ADDRESS,RESULT from STUDENTS")
for row in cursor:
    print ("ID =", row[0], sep="" , end="\t")
    print ("NAME =", row[1], sep=" ", end="\t")
    print ("ADDRESS =", row[2], sep=" ", end="\t")
    print ("Result =", row[3], sep=" ", end="\t")
    print()
conn.close()