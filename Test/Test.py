
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql as my
from mysql import connector
from tkinter import *

def show():

    # tempList = [['Jim', '0.33', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67'], 
    # ['Dave', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67'], 
    # ['James', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67'], 
    # ['Eden', '0.5', '0.67', '0.67', '0.67', '0.67', '0.67', '0.67']]
    # tempList.sort(key=lambda e: e[1], reverse=True)

    # tempList = [
    #     (1355, 'sdfsdf', 456564546, 'A+', 45.23, 45.23, 45.23, 45.23, 45.23, 45.23, 45.23, 45.23, 45.23, 45.23), #14
    #     (1422, 'someone', 951475369, 'B+', 14.12, 14.12, 14.12, 14.12, 14.12, 14.12, 14.12, 14.12, 14.12, 14.12),
    #     (1647, 'fdf', 123, 'B-', 17.2, 17.2, 17.2, 17.2, 17.2, 17.2, 17.2, 17.2, 17.2, 17.2),
    #     (1716, '12.12', 123456789, 'B-', 12.12, 12.12, 12.12, 12.12, 12.12, 12.12, 12.12, 12.12, 12.12, 12.12),
    #     (1971, 'asdasd', 123465789, 'A+', 124.12, 124.12, 124.12, 124.12, 124.12, 124.12, 124.12, 124.12, 124.12, 124.12)
    # ]
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

    count = 1
    for i, (name, score, a, b, c, d, e, f, g, h, i ,j , k, l ) in enumerate(result, start=1):
        listBox.insert('', END, values=(count, name, score, a, b, c, d, e, f, g, h, i ,j , k, l))
        count += 1

    # listBox.geometry("0x0")
    # listBox.config(anchor=CENTER)

    # listBox.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=listBox.yview)
    

scores = tk.Tk() 

scrollbar = Scrollbar(scores)
# scrollbar.grid(row = 2, column = 3)  
scrollbar.grid()


label = tk.Label(scores, text="Patient Details", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('No', 'Patirnt ID', 'Name', 'Phone No', 'Blood Group', 'F B S', 'P P B S', 'B P', 'Creatinine', 'T3', 'T4', 'T S H', 'A S T', 'A L T', 'A L P')
listBox = ttk.Treeview(scores, columns=cols, show='headings')

style = ttk.Style(scores)
style.configure('Treeview', rowheight=60)
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=3)



# listBox.grid(row=2,column=0,padx=5,pady=5,sticky='nsew',side = LEFT )   
# listBox.pack( ) 
# listBox.pack(expand=True)

scores.state('zoomed')
# listBox.state('zoomed')
# listBox.configure(justify=RIGHT)

scores.geometry("0x0")

showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

scores.mainloop()





#---------------------------------------------------------------------------------------------------------------------------------------------------





# import tkinter as tk
# from tkinter import ttk

# class Scrollable(tk.Frame):
#     """
#        Make a frame scrollable with scrollbar on the right.
#        After adding or removing widgets to the scrollable frame, 
#        call the update() method to refresh the scrollable area.
#     """

#     def __init__(self, frame, width=16):

#         scrollbar = tk.Scrollbar(frame, width=width)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

#         self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
#         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         scrollbar.config(command=self.canvas.yview)

#         self.canvas.bind('<Configure>', self.__fill_canvas)

#         # base class initialization
#         tk.Frame.__init__(self, frame)         

#         # assign this obj (the inner frame) to the windows item of the canvas
#         self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


#     def __fill_canvas(self, event):
#         "Enlarge the windows item to the canvas width"

#         canvas_width = event.width
#         self.canvas.itemconfig(self.windows_item, width = canvas_width)        

#     def update(self):
#         "Update the canvas and the scrollregion"

#         self.update_idletasks()
#         self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))

        
# root = tk.Tk()

# header = ttk.Frame(root)
# body = ttk.Frame(root)
# footer = ttk.Frame(root)
# header.pack()
# body.pack()
# footer.pack()

# ttk.Label(header, text="The header").pack()
# ttk.Label(footer, text="The Footer").pack()


# scrollable_body = Scrollable(body, width=32)

# for i in range(30):
#     ttk.Button(scrollable_body, text="I'm a button in the scrollable frame").grid()

# scrollable_body.update()

# root.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------
# from tkinter import *



# def prt():
#     print(variable.get())

# window = Tk()
# window.resizable(0,0)
# bloodGroups = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
# variable = StringVar(window)
# variable.set("Select Blood Group")
# w = OptionMenu(window, variable, *bloodGroups)
# w.config(font = ("Times New Roman", 16))
# w.pack()

# Btn = Button(window, text ="Submit", bd = 6, font = ("Open Sans", 16), command = prt)
# Btn.pack()
# Btn.place(x = 380, y = 460, height = 50, width = 100)

# window.title("Patient Medical Report")
# window.geometry("1050x550")
# window.mainloop()

# w.place(x = 790, y = 157, height = 28, width = 200)







#---------------------------------------------------------------------------------------------------------------------------------------------------









# import tkinter
# from tkinter import messagebox

# # hide main window
# root = tkinter.Tk()
# root.withdraw()

# # message box display
# messagebox.showerror("Error", "Patient-ID could not be generated please contact the developer")
# messagebox.showwarning("Warning","Warning message")
# messagebox.showinfo("Information","Informative message")


#---------------------------------------------------------------------------------------------------------------------------------------------------


# from tkinter import *
# class All:
#     def __init__(self, x):
# win = x
# t1 = Entry(bd=3)
# t1.place(x=150,y=150)
#         # self.t2 = Entry(bd=3)
#         # self.t2.place(x=200,y=200)
# b1 = Button(self.win, text='Show', command=self.clear)
# b1.pack()


#     def clear(self):
#         lbl = Label(self.win, text = str(self.t1.get()) ,font = ("Times New Roman", 26))
#         lbl.place(x=250,y=250)
# t1.delete(0, 'end')
# t1.insert(END, "")


# window = Tk()
# All(window)
# # ubj.add(window)
# window.title('Hello Python')
# window.geometry("1000x1000")
# window.mainloop()





#---------------------------------------------------------------------------------------------------------------------------------------------------




# from tkinter import *


# class MyWindow:
#     def __init__(self, win):
# lbl1 = Label(win, text='First number')
# lbl2 = Label(win, text='Second number')
# lbl3 = Label(win, text='Result')
# t1 = Entry(bd=3)
# t2 = Entry()
# t3 = Entry()
# btn1 = Button(win, text='Add')
# btn2 = Button(win, text='Subtract')
# lbl1.place(x=100, y=50)
# t1.place(x=200, y=50)
# lbl2.place(x=100, y=100)
# t2.place(x=200, y=100)
# b1 = Button(win, text='Add', command=self.add)
# b2 = Button(win, text='Subtract')
# b2.bind('<Button-1>', self.sub)
# b1.place(x=100, y=150)
# b2.place(x=200, y=150)
# lbl3.place(x=100, y=200)
# t3.place(x=200, y=200)

#     def add(self):
# t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1+num2
# t3.insert(END, str(result))

#     def sub(self, event):
# t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1-num2
# t3.insert(END, str(result))


# window = Tk()
# MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------

# import tkinter  as tk

# root=tk.Tk()


# canvas1 = tk.Canvas(root, width = 400, height = 300)
# canvas1.pack()

# # username = tk.Entry(root)
# # canvas1.create_window(200,140, window=username)
# # canvas1.create_text(100,140,fill="darkblue",text="username")

# # password = tk.Entry(root)
# # canvas1.create_window(200,180,window=password)
# # canvas1.create_text(100,180,fill="darkblue",text="password")

# variable = tk.StringVar(canvas1)
# variable.set("Facebook")

# w=tk.OptionMenu(root , variable, "Facebook","Twitter","Spotify","Swiggy")
# w.pack()

# button1= tk.Button(text='Go')
# canvas1.create_window(250,250, window=button1)

# root.mainloop()