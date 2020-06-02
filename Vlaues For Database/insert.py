import mysql as my
from mysql import connector
import pandas as pd
from random import randint as ri
from random import uniform as rf
import time as t

def genRandInt():
   
       
        global result
        while True:
            r = ri(1,100000000)
            if  r not in result:
                break

        result.append(r) 
        return r

def genrandphno():
    templst = [9]
    for i in range(9):
        templst.append(ri(0,8)) 

    templst = int(''.join([str(e) for e in templst]))
    return templst

def randomSample():
    return round(rf(5.2,12.9),2)

def randbs():
    lst = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    return lst[ri(0,(len(lst) - 1))]


mydb = my.connector.connect( host = '127.0.0.1', user = 'root', password = '', database = 'patient')

try:
    cur = mydb.cursor()
    cur.execute("SELECT ID FROM patient")
    result = cur.fetchall()
    cur.close()
except Exception as e:
        print(e)

df = pd.read_csv('F:/Studies/6/Project/Python-Project/Vlaues For Database/baby.csv')

i = 30000
while i <= len(df):
    cur2 = mydb.cursor()
    idd = genRandInt()
    name = str(df['name'][i])
    phno = genrandphno()
    blgrp = str(randbs())
    fbs = float(randomSample())
    ppbs = float(randomSample())
    bp = float(randomSample())
    creat = float(randomSample())
    t3 = float(randomSample())
    t4 = float(randomSample())
    tsh = float(randomSample())
    ast = float(randomSample())
    alt = float(randomSample())
    alp =float(randomSample())
    try:
        sql = "INSERT INTO patient VALUES ({},\'{}\',{},\'{}\',{},{},{},{},{},{},{},{},{},{})".format(idd,name,phno,blgrp,fbs,ppbs,bp,creat,t3,t4,tsh,ast,alt,alp)
        print(sql)
        print(i)
        cur2.execute(sql)
        cur2.close()
        mydb.commit()
        i += 1
    except:
        print("""LOL
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          .
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          .
          
          
          
          
          
          
          
          
          .
""")  
        t.sleep(2)

    
