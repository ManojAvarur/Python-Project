from tkinter import *
from tkinter import messagebox
import mysql as my
from mysql import connector

class Display:

    def table(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM patient")
        result = cur.fetchall()
        total_rows = len(result)
        total_columns = len(result[0])

        count = 0    
        for i in range(total_rows):
            for j in range(total_columns):
                if count < 1:
                    self.e = Label(root,text = "ID", width=10, fg='black', bd = 5, font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j) 

                count += 1
                # txt = Text(root)
                # txt.insert(INSERT, "--------------------------------------------------------------------------------------")
                # txt.grid(row=i) 
                self.e = Label(root,text = result[i][j], width=10, fg='black', bd = 5, font=('Arial',16,'bold')) 
                self.e.grid(row=i, column=j) 
                # self.e.insert(END, result[i][j])
                # self.e.config(state = 'disabled')


try:
    op = open("bin\pass.txt")
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

# If you are runiing this in a Ubuntu use the bellow code
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

obj = Display()
obj.table()

root.mainloop()