import requests
import urllib
import datetime
import pymysql
import time
import json

conn = None
cur = None

sql = ""

conn = pymysql.connect(host='ipmango.synology.me', port=5010, user='sykwon36', password='Tnduf89919*',db='pythonDB', charset='utf8' )
cur = conn.cursor()

token = 'alBi5OAo3eYx95nfmxRhoHr4FycAQPWjKa3EmRk4JIB'

def dbGet():
    cur.execute("SELECT * FROM userTable")
    while(True):
        
        row = cur.fetchone()
        if row == None:
            break
        Date = []
        if(json.loads(row[0], strict = False) == '')
        Date.append(json.loads(row[0], strict = False))
        Lunch = []
        Lunch.append(json.loads(row[1], strict = False))

    return (Date, Lunch)

def send():
    url = 'https://notify-api.line.me/api/notify'
    Date = []
    Lunch = []
    Date, Lunch = dbGet()
    obj = {
        'day' : Date[0],
        'menu' : Lunch[0]
    }
    
    today = datetime.datetime.today().weekday()
    print(obj['day'])
    # payload = obj['day'][today]
    # print(payload, 1)
    #response = requests.request("POST", url, data = )
    
    return

send()