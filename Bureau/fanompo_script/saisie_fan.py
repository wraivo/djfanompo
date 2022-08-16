
import sqlite3
from outils import *

memb = int(input("Omeo ny membre n° : "))
serv = int(input("Omeo ny service n° : "))

db=sqlite3.connect('fanompo.db')
mqr="select m.Fiantso from membres m where membID=?"
sqr="select s.anarFohy from services s where numSVC=?"
qry="insert into fanome(mb, svc) values(?,?);"
def insert():
    try:
        cur=db.cursor()
        cur.execute(qry, (memb,serv))
        db.commit()
        print ("records added successfully")
    except:
        print ("error in operation")
        db.rollback()

def check():
    try:
        cur=db.cursor()
        cur.execute(mqr, (memb,))
        mb=cur.fetchone()
        cur.execute(sqr, (serv,))
        sv=cur.fetchone()
        print ("service : ",sv)
        print("membre : ",mb)        
    except:
        print ("error in operation")
        db.rollback()

# check()
# chk = int(input("OK ve? (1 raha eny): "))
# if chk==1:
#     insert()
# else:
#     print("Avereno ary")




db.close()


