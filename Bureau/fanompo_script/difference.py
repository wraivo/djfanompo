import sqlite3

def getDeveloperName():
    s_id = int(input('Isan ny sabata dinganina: ' ) or "2")

    try:
        sqliteConnection = sqlite3.connect('/home/wnaina/Bureau/fanompo_script/fanompo.db')
        cursor = sqliteConnection.cursor()
        datyq="select distinct c.Daty from calend c order by c.Daty desc limit ?"

        cursor.execute(datyq, (s_id,))
        daty=cursor.fetchall()
        datyx=''
        ddjoin=''
        i=0
        for d in daty:
            i=i+1
            if i-1 < len(daty):
                ddjoin=' or c.Daty= '
            else:
                ddjoin=''
            dd=d[0]
            datyx=datyx+"'"+dd+"'"+ddjoin
        
        datyx=datyx[:-12] # manala ny 'or c.Daty ' farany
            
        # print(datyx)
        diff_query = "select m.Fiantso from membres m where Tsyeo=False except "+"SELECT distinct m.Fiantso from membres m join calend c on m.membID=c.mbID \
        where c.Daty = "+datyx + "order by m.Fiantso"


        cursor.execute(diff_query)
        names = cursor.fetchall()
        print("Nombre: ", len(names))
        i=0
        for n in names:
            i=i+1
            print(i,' ',n[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:        
            sqliteConnection.close()

getDeveloperName()

