# Database Practice
import sqlite3

# Connection allows us to connect python to an SQL database
connection = sqlite3.connect("./database.db")
# cursor allows us to interacte with the SQL DB
cursor = connection.cursor()

query = """
SELECT AVG(price) FROM Products;
"""

result = cursor.execute(query).fetchall()
print(f"SQL RESULT: {result}")

#BOTTOM/END OF OUR CODE
connection.commit() # commits changes
connection.close()  # disconnects connection