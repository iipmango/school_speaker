import pymysql
import time
import json

conn = None
cur = None

sql = ""

conn = pymysql.connect(host='ipmango.synology.me', port=5010, user='sykwon36', password='Tnduf89919*',db='pythonDB', charset='utf8' )
cur = conn.cursor()
def dbInsert(menu_date, menu):
    sql = "INSERT INTO userTable VALUES('" + menu_date + "','" + menu + "'," + "CURRENT_TIMESTAMP" + ")"
    cur.execute(sql)
    conn.commit()
    conn.close()

def dbGet():
    cur.execute("SELECT * FROM userTable")
    while(True):
        
        row = cur.fetchone()
        if row == None:
            break
        Date = []
        Date.append(json.loads(row[0], strict = False))
        Lunch = []
        Lunch.append(json.loads(row[1], strict = False))

    return (Date, Lunch)
     
