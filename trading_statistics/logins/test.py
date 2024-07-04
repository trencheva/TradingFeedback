import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

my_cursor = db.cursor()
# my_cursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# my_cursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ('Shanan', datetime.now(), 'F'))

# my_cursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

my_cursor.execute("DESCRIBE Test")
for x in my_cursor:
    print(x)

my_cursor.fetchall()