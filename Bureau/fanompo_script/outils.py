from datetime import datetime
import sqlite3
import sys

try:
        sqliteConnection = sqlite3.connect('/home/wnaina/Bureau/fanompo_script/fanompo.db')
        cursor = sqliteConnection.cursor()
except:
        print("misy erreur")

def dateformat(dt):
    date_string = '2018-12-25'

    format = "%Y-%m-%d"

    try:

      datetime.strptime(date_string, format)

      return True

    except ValueError:

      return False

def issabbath(datep):

    # date_str = '10-27-2020'

    dto = datetime.strptime(datep, '%Y-%m-%d').date()

    # If today is Sunday (1 = Mon, 2 = Tue, 3 = Wen ...)
    if dto.isoweekday() == 6:
        return True
    else:
        return False

# datec = str(sys.argv[1])
# datecv = datetime.strptime(datec, '%Y-%m-%d')
# sb=issabbath(datecv)

def isdatevalid(datec):
    if dateformat(datec) and issabbath(datec):
        return True
    else:
        return False

def isvalidmembser(serv : int, memb : int):    
        fanome_query = "SELECT membID from membres m \
        join fanome f on m.membID = f.mb JOIN services s on \
        f.svc = s.numSVC where f.svc=?"
        cursor.execute(fanome_query,(serv,))
        membserv=cursor.fetchall()
        mblist=[membserv[i][0] for i in range(len(membserv))]
        if memb in mblist:
            return True
        else:
             return False


def isvalidserv(serv : int):    
        fanome_query = "SELECT numSVC from services s"
        cursor.execute(fanome_query)
        servl=cursor.fetchall()
        servlist=[servl[i][0] for i in range(len(servl))]
        if serv in servlist:
            return True
        else:
             return False
         

print(isvalidmembser(4,15))