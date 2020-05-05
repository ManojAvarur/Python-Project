from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql as my
from mysql import connector

class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame, 
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)         

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))



def table():
        cur = mydb.cursor()
        cur.execute("SELECT * FROM patient")
        result = cur.fetchall()
        total_rows = len(result)
        total_columns = len(result[0])
        scrollable_body = Scrollable(body, width=32)
        for i in range(total_rows):
            for j in range(total_columns):
                e = ttk.Entry(scrollable_body, width=10, fg='blue', bd = 5, font=('Arial',16,'bold')) 
                e.grid(row=i, column=j) 
                e.insert(END, result[i][j])
                e.config(state = 'disabled')


try:
    op = open("Password\pass.txt")
    usr = op.readline().replace('\n','')
    pwd = op.readline().replace('\n','')

    mydb = my.connector.connect(host="127.0.0.1", user=usr, password=pwd , database="patient")
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
header = ttk.Frame(root)
body = ttk.Frame(root)
footer = ttk.Frame(root)
header.pack()
body.pack()
footer.pack()

# If you are runiing this in a Windows use the bellow code
root.state('zoomed')

# If you are runiing this in a Ubuntu use the bellow code
# root.attributes('-zoomed', True)





# root.overrideredirect(True)
# root.overrideredirect(False)
# root.attributes('-fullscreen',True)

# sb = Scrollbar(root)  
# sb.pack(side = RIGHT, fill = Y)  

root.title("Patient Medical Report")
root.geometry("1000x1000")


table()

root.mainloop()