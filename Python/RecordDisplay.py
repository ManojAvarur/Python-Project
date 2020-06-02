import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql as my
from mysql import connector
from tkinter import *
import os
import threading as t


class myThread(t.Thread):
    def __init__(self):
        t.Thread.__init__(self)
    
    def run(self):
        os.system("Python\PatientRecordDisplay.py")

class Display:
    
    def __init__(self,lp):
        self.listBox = lp
        self.disp()
        

    def disp(self):
        count = 1
        for i, (name, score, a, b, c, d, e, f, g, h, i ,j , k, l ) in enumerate(result, start=1):
            listBox.insert('', END, values=(count, name, score, a, b, c, d, e, f, g, h, i ,j , k, l))
            # btn = Button(root, text = "Submit", bd = 6, font = ("Open Sans", 16), command = None)
            count += 1

        # selection = self.listBox.get(self.listBox.curselection()[0])
        # print(selection)
        self.listBox.bind('<Double-1>', self.selection)

    def selection(self, event):

        temp = str(self.listBox.item(self.listBox.selection())['values'][1])

        if os.path.exists("bin/recordDisp.txt"):
            os.remove("bin/recordDisp.txt")

        op = open('bin/recordDisp.txt','w')
        op.write(temp)
        op.close() 

        tobj = myThread()
        tobj.start()
        # print( self.listBox.item(self.listBox.selection())['values'][1] )






# Start ---------------------------------------------------------
try:
        op = open("bin\pass.txt")
        usr = op.readline().replace('\n','')
        pwd = op.readline().replace('\n','')

        mydb = my.connector.connect(host="127.0.0.1", user=usr, password=pwd, database="patient")

        cur = mydb.cursor()
        cur.execute("SELECT * FROM patient")
        result = cur.fetchall()

except Exception as e:
        error = """Check Your Connection
        1. MySQL Servers
        2. User-ID or Password maybe incorrect
        3. Re-Connect using diffrent User-Id and Password
        
    {}""".format(e)
        print(e)
        messagebox.showerror("Error",error)
        exit()







root = Tk()

frame1 = Frame(root)


frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(root)
frame2.pack(side=tk.BOTTOM, fill=tk.X)

style = ttk.Style(frame1)
style.configure('Treeview.Heading',  font = ('Times New Roman',20,'bold'), bd =  5)
style.configure('Treeview', rowheight=60, font = ('Times New Roman',16))

cols = ('No', 'Patirnt ID', 'Name', 'Phone No', 'Blood Group', 'F B S', 'P P B S', 'B P', 'Creatinine', 'T3', 'T4', 'T S H', 'A S T', 'A L T', 'A L P')
listBox = ttk.Treeview(frame1, columns=cols, show='headings')


for col in cols:
    listBox.heading(col, text=col) 
    listBox.column(col, anchor=CENTER) 
listBox.grid(row=1, column=0, columnspan=1)

listBox.pack(fill=BOTH,expand=1)



Display(listBox)

scrollH = tk.Scrollbar(frame2, orient=tk.HORIZONTAL)
scrollH.config(command=listBox.xview)
listBox.configure(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)



root.state('zoomed')
root.mainloop()