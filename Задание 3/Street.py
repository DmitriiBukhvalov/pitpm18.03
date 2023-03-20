import sqlite3
 
db = sqlite3.connect('mydatabase.db')

c = db.cursor()


#c.execute("""CREATE TABLE city(
#    street text
#)""")

c.execute("SELECT * FROM city")
print(c.fetchall())

db.commit()

db.close()
