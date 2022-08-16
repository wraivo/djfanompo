import pandas as pd
import sqlite3
from tabulate import tabulate
import sys

s_id = int(sys.argv[1])

# s_id = input('Membre ID:')

def getDeveloperName(id):
    try:
        sqliteConnection = sqlite3.connect('/home/wnaina/Bureau/fanompo_script/fanompo.db')
        cursor = sqliteConnection.cursor()
        select_query = "SELECT * FROM membres where membID = ?"
        fanome_query = "SELECT s.numSVC, s.anarFohy from services s join fanome f on s.numSVC = f.svc where f.mb=? "
        memb_query = "SELECT max(c.Daty), m.Fiantso, s.numSVC, s.anarFohy from membres m \
        join calend c on m.membID = c.mbID JOIN services s on \
        c.svcID = s.numSVC where c.mbID=? group by s.anarFohy order by c.Daty desc"
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print(name[0],name[1])
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        cursor.execute(fanome_query, (id,))
        fanome = cursor.fetchall()
        dff=pd.DataFrame(fanome)
        print(tabulate(dff))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        cursor.execute(memb_query, (id,))
        memb = cursor.fetchall()   
        df = pd.DataFrame(memb)     
        print(tabulate(df, headers=["Daty","Fiantso","numSVC", "Service"]))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:        
            sqliteConnection.close()

getDeveloperName(s_id)