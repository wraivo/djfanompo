import sqlite3

connection = sqlite3.connect("fanompo.db")
cursor = connection.cursor()
cursor.execute("""
    SELECT c.Daty, m.Fiantso, s.anarFohy FROM membres m 
    join calend c on m.membID=c.mbID join services s on c.svcID=s.numSVC ;
    """)
results = cursor.fetchall()
for r in results:
    print(r)
cursor.close()
connection.close()