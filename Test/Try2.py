import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql as my
from mysql import connector
from tkinter import *

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
        print( self.listBox.item(self.listBox.selection())['values'][1] )

    
def pnt(event):
    print(Listbox.item(listBox.selection()))


try:
        op = open("Password\pass.txt")
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






# Start ---------------------------------------------------------
root = Tk()

frame1 = Frame(root)
# top_frame = tk.Frame(root)
    # top_frame.pack(sid="top")
    # bot_frame = tk.Frame(root)
    # bot_frame.pack(sid="bottom")

    # tk.Label(top_frame, text="Row 0 of top_frame").grid(row=0, column=0)

    # tk.Label(bot_frame, text="Row 0 of bot_frame").grid(row=0, column=0)
    # tk.Label(bot_frame, text="Row 1 of bot_frame").grid(row=1, column=0)
    # tk.Label(bot_frame, text="Row 2 of bot_frame").grid(row=2, column=0)
    # tk.Button(bot_frame, text="Row 3 of bot_frame").grid(row=3, column=0)

frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(root)
frame2.pack(side=tk.BOTTOM, fill=tk.X)


# frame1.grid(row=0,column=0,sticky='nsew')
    # frame1.columnconfigure(0,weight=0)
    # frame1.rowconfigure(0,weight=0)
        # frame1.pack(fill=BOTH,expand=1)

    # listbox = Listbox(frame1)
        # listbox.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
        # listbox.config(width=50,height=10)

style = ttk.Style(frame1)
style.configure('Treeview.Heading',  font = ('Times New Roman',20,'bold'), bd =  5)
style.configure('Treeview', rowheight=60, font = ('Times New Roman',16))

cols = ('No', 'Patirnt ID', 'Name', 'Phone No', 'Blood Group', 'F B S', 'P P B S', 'B P', 'Creatinine', 'T3', 'T4', 'T S H', 'A S T', 'A L T', 'A L P', 'Select')
listBox = ttk.Treeview(frame1, columns=cols, show='headings')


for col in cols:
    listBox.heading(col, text=col) 
    listBox.column(col, anchor=CENTER) 
listBox.grid(row=1, column=0, columnspan=1)

listBox.pack(fill=BOTH,expand=1)



Display(listBox)

# Listbox.bind('<Button-1>', pnt)
# Listbox.bind('<Double-1>', quit) 


scrollH = tk.Scrollbar(frame2, orient=tk.HORIZONTAL)
scrollH.config(command=listBox.xview)
listBox.configure(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)



root.state('zoomed')
root.mainloop()