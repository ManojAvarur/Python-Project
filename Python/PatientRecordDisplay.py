# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# from matplotlib import style
from pandas import DataFrame
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas_profiling import ProfileReport as pr
import threading as t
# import time as t
import os
from tkinter import *
import mysql as my
from mysql import connector
from tkinter import messagebox, ttk
import shutil as sl
import webbrowser as wb
import subprocess as sp

mlt.rcParams['savefig.pad_inches'] = 0

class myThreads(t.Thread):
    def __init__(self, fn):
        t.Thread.__init__(self)
        self.filename = fn

    def run(self):
        # wb.open('file://' + self.filename, new = 2)
        try: # should work on Windows
            os.startfile(self.filename)
        except AttributeError:
            try: # should work on MacOS and most linux versions
                sp.call(['open', self.filename])
            except:
                print('Could not open URL')

def askmsg():

    # t.sleep(3)
    cur = mydb.cursor()
    cur.execute("SELECT * FROM patient WHERE ID = %d" % uid)
    result2 = cur.fetchall()
    result3 = str(result2)
    result3 = result3.replace('[','')
    result3 = result3.replace(']','')
    result3 = result3.replace('(','')
    result3 = result3.replace(')','')
    result3 = result3.replace("'",'\"')
    cur.close()
    

    parent_dir = "Patient Records"
    strr = " \"ID\",\"NAME\",\"PHONE_NO\",\"BLOOD_GROUP\",\"FBS\",\"PPBS\",\"BP\",\"CREATININE\",\"T3\",\"T4\",\"TSH\",\"AST\",\"ALT\",\"ALP\"" 
    msgbx = messagebox.askquestion('Information','Do you want to generate report!', icon ='question')

    if msgbx == 'yes':

        if not os.path.exists(parent_dir):
            os.mkdir(parent_dir)
            
        path = os.path.join(parent_dir,str(uid))

        if os.path.exists(path):
            sl.rmtree(path)
                
        os.mkdir(path)

        print(path)
        op = open(path+'\\details-{}.csv'.format(uid),'w')
        op.write(strr)
        op.write('\n')
        op.write(result3)
        op.close()
        
        messagebox.showinfo('Information','You\'r report will be generated in 10s' )

        df = pd.read_csv(path+'\\details-{}.csv'.format(uid))
        profiling = pr(df)
        profiling.to_file(output_file = path+'\\details-{}.html'.format(uid))

        path2 = os.path.join(path,'details-{}.html'.format(uid))
        print(path2)
        obj = myThreads(path2)
        obj.start()

        

try:
        op = open("bin\pass.txt")
        usr = op.readline().replace('\n','')
        pwd = op.readline().replace('\n','')
        op.close()

        op = open("bin/recordDisp.txt")
        uid = int(op.readline().replace('\n',''))
        op.close()

        mydb = my.connector.connect(host="127.0.0.1", user=usr, password=pwd, database="patient")

        cur = mydb.cursor()
        cur.execute("SELECT FBS, PPBS, BP, CREATININE, T3, T4, TSH, AST, ALT, ALP FROM patient WHERE ID = %d" % uid)
        result = cur.fetchall()
        cur.close()

        tmp_lst = []

        for i in result[0]:
            tmp_lst.append(i)

        # tmp_lst.append(13)
        cur = mydb.cursor()
        cur.execute("SELECT NAME, PHONE_NO, BLOOD_GROUP FROM patient WHERE ID = %d" % uid)
        result = cur.fetchall()
        cur.close()

        count = 0
        tmpStrng = str(result[0][count])
        count += 1

except Exception as e:
        error = """Check Your Connection
        1. MySQL Servers
        2. User-ID or Password maybe incorrect
        3. Re-Connect using diffrent User-Id and Password
        
    {}""".format(e)
        print(e)
        messagebox.showerror("Error",error)
        exit()

root= Tk(className= (" Name  :   ' " + tmpStrng + " '  Patient Details ") ) 
# root.configure(bg='white')

frame1 = Frame(root, background='white', bd=-2)
frame1.pack(side=TOP, expand=True, fill = BOTH)

frame2 = Frame(root, bd=-2, background='white')
frame2.pack(side=BOTTOM, fill = BOTH, expand=True)



Label(frame1, text = ("Patient Name : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 100, y = 50)

tmpStrng = str(result[0][count])
count += 1

Label(frame1, text = ("Phone Number : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 800, y = 50)

tmpStrng = str(result[0][count])
count += 1

Label(frame1, text = ("Blood Group : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 1600, y = 50)




data = {
    'Tests': ['FBS', 'PPBS', 'BP', 'CREATININE', 'T3', 'T4', 'TSH', 'AST', 'ALT', 'ALP']
}

data['Results'] = tmp_lst

df1 = DataFrame(data,columns=['Tests','Results'])
# print(tmp_lst)


  
figure1 = plt.Figure(figsize=(9,8), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, frame2)
bar1.get_tk_widget().pack(anchor=CENTER, side=BOTTOM)
df1 = df1[['Tests','Results']].groupby('Tests').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Results')

root.state('zoomed')

askmsg()

root.mainloop()
