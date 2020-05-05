from tkinter import *
import os
from tkinter import messagebox
import mysql as my
from mysql import connector
from concurrent import futures


class AllMainFunctions:

    def realcallback(self):
        os.system(self.filename)

    def callBack(self, val):

        if val == 1:
            self.filename = "Python\MedicalManagement.py"   
            root.after(3, self.realcallback)
           

        elif val == 2:
            self.filename = "Python\MedicalManagement.py"
            root.after(3, self.realcallback)

        else:
            exit()

    def Buttons(self):

        btn = Button(root, text = "Insert New Patient Details", bd = 6, font = ("Open Sans", 16), command = lambda: self.callBack(1))
        btn.pack()
        btn.place(x = 110, y = 150)

        btn = Button(root, text = "View Patient Details", bd = 6, font = ("Open Sans", 16), command = lambda: self.callBack(2))
        btn.pack()
        btn.place(x = 140, y = 250)

        btn = Button(root, text = "Exit", bd = 6, font = ("Open Sans", 16), command = lambda: self.callBack(3))
        btn.pack()
        btn.place(x = 200, y = 350, width = 100)


    def validate(self):
        
        try:
            ud = str(self.txtfld_1.get())
            pd = str(self.txtfld_2.get())
            mydb = my.connector.connect(host="127.0.0.1", user = ud, password = pd , database="patient")
            mydb.close()
            self.lbl.destroy()
            self.lbl1.destroy()
            self.txtfld_1.destroy()
            self.txtfld_2.destroy()
            self.btn.destroy()

            if os.path.exists("Password\pass.txt"):
                os.remove("Password\pass.txt")

            op = open('Password\pass.txt','w')
            op.write(ud)
            op.write("\n")                   
            op.write(pd)
            op.close() 
            mydb.close()
            self.Buttons()
            
        except Exception as e:
            if str(e) == "2003: Can't connect to MySQL server on '127.0.0.1:3306' (10061 No connection could be made because the target machine actively refused it)":
                messagebox.showerror("Database Connection Error!","Connection to the database could not be established")
            else:  
                error = "Invalid username or password"
                messagebox.showwarning("Warning",error)


    def LoginCheck(self):

        self.lbl1 = Label(root, text = "User Name : ", font = ("Times New Roman", 16))
        self.lbl1.place(x = 70, y = 200)
        self.txtfld_1 = Entry(root, bd = 1.5, font = ("Times New Roman", 16))
        self.txtfld_1.place(x = 190, y = 202, height = 25, width = 200)

        self.lbl = Label(root, text = "Password : ", font = ("Times New Roman", 16))
        self.lbl.place(x = 85, y = 250)
        self.txtfld_2 = Entry(root, bd = 1.5, font = ("Times New Roman", 16))
        self.txtfld_2.place(x = 190, y = 252, height = 25, width = 200)

        self.btn = Button(root, text = "Submit", bd = 6, font = ("Open Sans", 16), command = self.validate)
        self.btn.pack()
        self.btn.place(x = 220, y = 300)

root = Tk()
root.resizable(0,0)
root.title("Patient Medical Report")
root.geometry("500x550")

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/3 - windowHeight)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

lbl11 = Label(root, text = "Patient Health Management System", font = ("Times New Roman", 22)) 
lbl11.place(x = 50, y = 25)  

lbl21 = Label(root, text = "______________________________________________________________________")  
lbl21.place(x = 75, y = 60, height = 13) 

lbl11 = Label(root, text = "© 2020 - 2050 JSSATEB. CSE. All Rights Reserved.", font = ("Open Sans", 10))
#lbl11.place(x = 75, y = 550, height = 15) 
lbl11.place(relx=0.81, rely=1.0, anchor='se')

obj = AllMainFunctions()
obj.LoginCheck()

root.mainloop()
