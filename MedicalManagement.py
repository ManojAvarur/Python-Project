from tkinter import *
from tkinter import messagebox
from random import randint as ri
import mysql as my
from mysql import connector

class AllMainFunctions:
    
    def clear_text( self ): 

        self.variable.set("Select Blood Group")

        self.txtfld_1.delete(0, 'end')
        # self.txtfld_1.insert(END, "")

        self.txtfld_2.delete(0, 'end')
        # self.txtfld_2.insert(END, "")

        self.txtfld_3.delete(0, 'end')
        # self.txtfld_3.insert(END, "")

        self.txtfld_4.delete(0, 'end')
        # self.txtfld_4.insert(END, "")

        self.txtfld_5.delete(0, 'end')
        # self.txtfld_5.insert(END, "")

        self.txtfld_6.delete(0, 'end')
        # self.txtfld_6.insert(END, "")

        self.txtfld_7.delete(0, 'end')
        # self.txtfld_7.insert(END, "")

        self.txtfld_8.delete(0, 'end')
        # self.txtfld_8.insert(END, "")

        self.txtfld_9.delete(0, 'end')
        # self.txtfld_9.insert(END, "")

        self.txtfld_10.delete(0, 'end')
        # self.txtfld_10.insert(END, "")

        self.txtfld_11.delete(0, 'end')
        # self.txtfld_11.insert(END, "")

        self.txtfld_12.delete(0, 'end')
        # self.txtfld_12.insert(END, "")

    def genRandInt( self ):

        
        try:
            cur = mydb.cursor()
            cur.execute("SELECT ID FROM patient")
            result = cur.fetchall()
        except Exception as e:
            messagebox.showerror("Error",e)
            exit()

        lists = []
        for row in result:
              lists.append(row[0])

        breakCheck = False
        count = 0
        while True:
            r = ri(1000,10000)
            count += 1
            # print(count)
            if not r in lists:
                break

            if count == 50:
                breakCheck = True
                break

        if breakCheck:    
            messagebox.showerror("Error", "Patient-ID could not be generated please contact the developer")
            exit()
            # cur.close()
            # return "ERROR 110"
        else:
            cur.close()
            return r       

    def bloodGroup(self, window ):
        bloodGroups = ["Select Blood Group","A+","A-","B+","B-","O+","O-","AB+","AB-"]
        self.variable = StringVar(window)
        self.variable.set(bloodGroups[0])
        self.w = OptionMenu(window, self.variable, *bloodGroups)
        self.w.config(font = ("Times New Roman", 16))
        self.w.pack()
        self.w.place(x = 790, y = 157, height = 28, width = 200)

    def patientIDgen(self):
        self.txtfld_0 = Entry(window, bd = 1.5,  font = ("Times New Roman", 16))
        self.txtfld_0.insert(0,self.genRandInt())
        self.txtfld_0.config(state = 'disabled')
        self.txtfld_0.place(x = 240, y = 98, height = 25, width = 200)
    
    def __init__(self, window):
        
        # ---------------------------------- Heading Row ----------------------------------------------------------------
            lbl = Label(window, text = "Enter Patient Details",font = ("Times New Roman", 26))
            lbl.place(x = 395, y = 10)
            lbl = Label(window, text = "----------------------------------",font = ("Times New Roman", 26))
            lbl.place(x = 350, y = 50, height = 25)

        # ---------------------------------- First Row ------------------------------------------------------------------
            lbl = Label(window, text = "Patient ID : ", font = ("Times New Roman", 20))
            lbl.place(x = 102, y = 90)
            self.patientIDgen()

            lbl = Label(window, text = "Name : ", font = ("Times New Roman", 20))
            lbl.place(x = 700, y = 90)
            self.txtfld_1 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_1.place(x = 790, y = 98, height = 25, width = 200)

        # ---------------------------------- Second Row -----------------------------------------------------------------
            lbl = Label(window, text = "Phone No : ", font = ("Times New Roman", 20))
            lbl.place(x = 105, y = 150)
            self.txtfld_2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_2.place(x = 240, y = 158, height = 25, width = 200)

            lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
            lbl.place(x = 620, y = 150)
            self.bloodGroup( window )

        # ---------------------------------- Third Row (Sugar Tests) ----------------------------------------------------
            lbl = Label(window, text = "FBS : ", font = ("Times New Roman", 20))
            lbl.place(x = 165, y = 210)
            self.txtfld_3 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_3.place(x = 240, y = 218, height = 25, width = 200)
            lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
            lbl.place(x = 440, y = 225) 

            lbl = Label(window, text = "PPBS : ", font = ("Times New Roman", 20))
            lbl.place(x = 700, y = 210)
            self.txtfld_4 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_4.place(x = 790, y = 218, height = 25, width = 200)
            lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
            lbl.place(x = 990, y = 225)

        # ---------------------------------- Forth Row ------------------------------------------------------------------
            lbl = Label(window, text = "Hypertension (BP) : ", font = ("Times New Roman", 20))
            lbl.place(x = 12, y = 270)
            self.txtfld_5 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_5.place(x = 240, y = 278, height = 25, width = 200)
            lbl = Label(window, text = " mm Hg", font = ("Open Sans",10))
            lbl.place(x = 440, y = 285)

            lbl = Label(window, text = "Creatinine : ", font = ("Times New Roman", 20))
            lbl.place(x = 650, y = 270)
            self.txtfld_6 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_6.place(x = 790, y = 278, height = 25, width = 200)
            lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
            lbl.place(x = 990, y = 285)

        # ---------------------------------- Fifth Row ------------------------------------------------------------------
            lbl = Label(window, text = "Thyroid : ", font = ("Times New Roman", 20))
            lbl.place(x = 130, y = 330)

            lbl = Label(window, text = "T3 = ", font = ("Times New Roman", 16))
            lbl.place(x = 270, y = 334)
            self.txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_7.place(x = 320, y = 338, height = 25, width = 100)
            lbl = Label(window, text = " ng/dL", font = ("Open Sans",10))
            lbl.place(x = 420, y = 341)

            lbl = Label(window, text = "T4 = ", font = ("Times New Roman", 16))
            lbl.place(x = 520, y = 334)
            self.txtfld_8 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_8.place(x = 570, y = 338, height = 25, width = 100)
            lbl = Label(window, text = " mIU/L", font = ("Open Sans",10))
            lbl.place(x = 670, y = 341)

            lbl = Label(window, text = "TSH = ", font = ("Times New Roman", 16))
            lbl.place(x = 775, y = 334)
            self.txtfld_9 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_9.place(x = 840, y = 338, height = 25, width = 100)
            lbl = Label(window, text = " mIU/L", font = ("Open Sans",10))
            lbl.place(x = 940, y = 341)

        # ---------------------------------- Sixth Row ------------------------------------------------------------------
            lbl = Label(window, text = "LFT : ", font = ("Times New Roman", 20))
            lbl.place(x = 170, y = 390)

            lbl = Label(window, text = "AST = ", font = ("Times New Roman", 16))
            lbl.place(x = 255, y = 394)
            self.txtfld_10 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_10.place(x = 320, y = 398, height = 25, width = 100)
            lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
            lbl.place(x = 420, y = 405)

            lbl = Label(window, text = "ALT = ", font = ("Times New Roman", 16))
            lbl.place(x = 505, y = 394)
            self.txtfld_11 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_11.place(x = 570, y = 398, height = 25, width = 100)
            lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
            lbl.place(x = 670, y = 405)

            lbl = Label(window, text = "ALP = ", font = ("Times New Roman", 16))
            lbl.place(x = 775, y = 394)
            self.txtfld_12 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
            self.txtfld_12.place(x = 840, y = 398, height = 25, width = 100)
            lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
            lbl.place(x = 940, y = 405)

        # ---------------------------------- Sevanth Row (Buttons)--------------------------------------------------------

            Btn = Button(window, text ="Submit", bd = 6, font = ("Open Sans", 16), command = self.insert)
            Btn.pack()
            Btn.place(x = 380, y = 460, height = 50, width = 100)

            Btn = Button(window, text ="Reset", bd = 6, font = ("Open Sans", 16), command = self.clear_text)
            Btn.pack()
            Btn.place(x = 580, y = 460, height = 50, width = 100)

    def insert( self ):
        check = False
        try:
            cur = mydb.cursor()
            idd = int(self.txtfld_0.get())
            name = str(self.txtfld_1.get())
            phno = int(self.txtfld_2.get())
            blgrp = str(self.variable.get())
            fbs = str(self.txtfld_3.get())
            ppbs = float(self.txtfld_4.get())
            bp = float(self.txtfld_5.get())
            creat = float(self.txtfld_6.get())
            t3 = float(self.txtfld_7.get())
            t4 = float(self.txtfld_8.get())
            tsh = float(self.txtfld_9.get())
            ast = float(self.txtfld_10.get())
            alt = float(self.txtfld_11.get())
            alp =float(self.txtfld_12.get())
            check = True
        except:
            messagebox.showwarning("Warning","Values can not be null")

        if check:  
            try:
                if blgrp == "Select Blood Group":
                    messagebox.showwarning("Warning", "Select Blood Group")
                else:
                    sql = "INSERT INTO patient VALUES ({},\'{}\',{},\'{}\',{},{},{},{},{},{},{},{},{},{})".format(idd,name,phno,blgrp,fbs,ppbs,bp,creat,t3,t4,tsh,ast,alt,alp)
                    print(sql)
                    cur.execute(sql)
                    mydb.commit()
                    cur.close()
                    self.clear_text()
                    self.txtfld_0.destroy()
                    self.patientIDgen()

            except Exception as e:
                error = "Values not inserted into database : {}".format(e)
                messagebox.showerror("Error",error)

try:
    mydb = my.connector.connect(host="127.0.0.1", user="root", passwd="", database="patient")
except Exception as e:
    error = """Check Your Connection
    1. MySQL Servers
    2. User-ID or Password
    3. {}""".format(e)
    messagebox.showerror("Error",error)
    exit()

window = Tk()
window.resizable(0,0)
AllMainFunctions(window)
window.title("Patient Medical Report")
window.geometry("1050x550")
window.mainloop()