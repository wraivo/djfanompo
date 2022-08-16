
import sqlite3


daty = input('Omeo daty (ex: 2022-08-27) : ')
memb = int(input("Omeo ny membre n° : "))
serv = int(input("Omeo ny service n° : "))

db=sqlite3.connect('fanompo.db')
qry="insert into calend(Daty, mbID, svcID) values(?,?,?);"
try:
    cur=db.cursor()
    cur.execute(qry, (daty,memb,serv))
    db.commit()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()

