import sqlite3

s_id = input('Service ID:')

def getDeveloperName(id):
    try:
        sqliteConnection = sqlite3.connect('/home/wnaina/Bureau/fanompo_script/fanompo.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        select_query = "SELECT * FROM services where numSVC = ?"
        fanome_query = "SELECT c.Daty, m.Fiantso, s.anarFohy from membres m \
        join calend c on m.membID = c.mbID JOIN services s on \
        c.svcID = s.numSVC where c.svcID=? "
        cursor.execute(select_query, (id,))
        name = cursor.fetchone()
        print("Developer Name is", name)
        cursor.execute(fanome_query, (id,))
        fanome = cursor.fetchall()
        for f in fanome:
            print(f)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:        
            sqliteConnection.close()
            print("sqlite connection is closed")

getDeveloperName(s_id)