import sqlite3
import pandas as pd
from tabulate import tabulate

s_id = input('Service ID:')

def getDeveloperName(id):
    try:
        sqliteConnection = sqlite3.connect('/home/wnaina/Bureau/fanompo_script/fanompo.db')
        cursor = sqliteConnection.cursor()
        select_query = "SELECT * FROM services where numSVC = ?"
        fanome_query = "SELECT max(c.Daty), m.membID, m.Fiantso, s.anarFohy from membres m \
        join calend c on m.membID = c.mbID JOIN services s on \
        c.svcID = s.numSVC where c.svcID=? group by m.Fiantso order by c.Daty desc"
        memb_query = "SELECT m.membID, m.Fiantso from membres m join fanome f on m.membID = f.mb \
        where f.svc=? "

        cursor.execute(select_query, (id,))
        name = cursor.fetchone()

        print(name)
        cursor.execute(fanome_query, (id,))
        fanome = cursor.fetchall()
        df=pd.DataFrame(fanome)
        cursor.execute(memb_query, (id,))
        memb = cursor.fetchall()
        dff=pd.DataFrame(memb)
        print("Isan ny Mpanao: ",len(memb))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print (tabulate(df,headers=["Daty","Fiantso","Service"]))
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print (tabulate(dff,headers=["Num","Fiantso"]))
        cursor.close()
        

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:        
            sqliteConnection.close()
            print("sqlite connection is closed")

getDeveloperName(s_id)