# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# from matplotlib import style
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import *
import mysql as my
from mysql import connector
from tkinter import messagebox, ttk


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
root.configure(bg='white')

# style = ttk.Style(root)
# style.configure('Label',  font = ('Times New Roman',20,'bold'), bd =  5) 

Label(root, text = ("Patient Name : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 100, y = 50)

tmpStrng = str(result[0][count])
count += 1

Label(root, text = ("Phone Number : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 800, y = 50)

tmpStrng = str(result[0][count])
count += 1

Label(root, text = ("Blood Group : " + tmpStrng), font = ("Times New Roman", 20,'bold'), bg='white').place(x = 1600, y = 50)


data = {
    'Tests': ['FBS', 'PPBS', 'BP', 'CREATININE', 'T3', 'T4', 'TSH', 'AST', 'ALT', 'ALP']
}

data['Results'] = tmp_lst

df1 = DataFrame(data,columns=['Tests','Results'])
# print(tmp_lst)


  
figure1 = plt.Figure(figsize=(9,9), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=BOTTOM, fill=BOTH)
df1 = df1[['Tests','Results']].groupby('Tests').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Results')

root.state('zoomed')

root.mainloop()