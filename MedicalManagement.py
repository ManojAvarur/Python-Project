from tkinter import *
from random import randint as ri

def genRandInt():
    return ri(1000,10000)

def bloodGroup( window ):
    bloodGroups = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    variable = StringVar(window)
    variable.set("Select Blood Group")
    w = OptionMenu(window, variable, *bloodGroups)
    w.config(font = ("Times New Roman", 16))
    w.pack()
    w.place(x = 790, y = 157, height = 28, width = 200)


def gui( window ):

# ---------------------------------- Heading Row ----------------------------------------------------------------
    lbl = Label(window, text = "Enter Patient Details",font = ("Times New Roman", 26))
    lbl.place(x = 395, y = 10)
    lbl = Label(window, text = "----------------------------------",font = ("Times New Roman", 26))
    lbl.place(x = 350, y = 50, height = 25)

# ---------------------------------- First Row ------------------------------------------------------------------
    lbl = Label(window, text = "Patient ID : ", font = ("Times New Roman", 20))
    lbl.place(x = 102, y = 90)
    txtfld_0 = Entry(window, bd = 1.5,  font = ("Times New Roman", 16))
    txtfld_0.insert(0,genRandInt())
    txtfld_0.config(state = 'disabled')
    txtfld_0.place(x = 240, y = 98, height = 25, width = 200)

    lbl = Label(window, text = "Name : ", font = ("Times New Roman", 20))
    lbl.place(x = 700, y = 90)
    txtfld_1 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_1.place(x = 790, y = 98, height = 25, width = 200)

# ---------------------------------- Second Row -----------------------------------------------------------------
    lbl = Label(window, text = "Phone No : ", font = ("Times New Roman", 20))
    lbl.place(x = 105, y = 150)
    txtfld_2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_2.place(x = 240, y = 158, height = 25, width = 200)

    lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
    lbl.place(x = 620, y = 150)
    bloodGroup( window )

# ---------------------------------- Third Row (Sugar Tests) ----------------------------------------------------
    lbl = Label(window, text = "FBS : ", font = ("Times New Roman", 20))
    lbl.place(x = 165, y = 210)
    txtfld_3 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_3.place(x = 240, y = 218, height = 25, width = 200)
    lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
    lbl.place(x = 440, y = 225) 

    lbl = Label(window, text = "PPBS : ", font = ("Times New Roman", 20))
    lbl.place(x = 700, y = 210)
    txtfld_4 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_4.place(x = 790, y = 218, height = 25, width = 200)
    lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
    lbl.place(x = 990, y = 225)

# ---------------------------------- Forth Row ------------------------------------------------------------------
    lbl = Label(window, text = "Hypertension (BP) : ", font = ("Times New Roman", 20))
    lbl.place(x = 12, y = 270)
    txtfld_5 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_5.place(x = 240, y = 278, height = 25, width = 200)
    lbl = Label(window, text = " mm Hg", font = ("Open Sans",10))
    lbl.place(x = 440, y = 285)

    lbl = Label(window, text = "Creatinine : ", font = ("Times New Roman", 20))
    lbl.place(x = 650, y = 270)
    txtfld_6 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_6.place(x = 790, y = 278, height = 25, width = 200)
    lbl = Label(window, text = " mg/dl", font = ("Open Sans",10))
    lbl.place(x = 990, y = 285)

# ---------------------------------- Fifth Row ------------------------------------------------------------------
    lbl = Label(window, text = "Thyroid : ", font = ("Times New Roman", 20))
    lbl.place(x = 130, y = 330)

    lbl = Label(window, text = "T3 = ", font = ("Times New Roman", 16))
    lbl.place(x = 270, y = 334)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 320, y = 338, height = 25, width = 100)
    lbl = Label(window, text = " ng/dL", font = ("Open Sans",10))
    lbl.place(x = 420, y = 341)

    lbl = Label(window, text = "T4 = ", font = ("Times New Roman", 16))
    lbl.place(x = 520, y = 334)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 570, y = 338, height = 25, width = 100)
    lbl = Label(window, text = " mIU/L", font = ("Open Sans",10))
    lbl.place(x = 670, y = 341)

    lbl = Label(window, text = "TSH = ", font = ("Times New Roman", 16))
    lbl.place(x = 775, y = 334)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 840, y = 338, height = 25, width = 100)
    lbl = Label(window, text = " mIU/L", font = ("Open Sans",10))
    lbl.place(x = 940, y = 341)

# ---------------------------------- Sixth Row ------------------------------------------------------------------
    lbl = Label(window, text = "LFT : ", font = ("Times New Roman", 20))
    lbl.place(x = 170, y = 390)

    lbl = Label(window, text = "AST = ", font = ("Times New Roman", 16))
    lbl.place(x = 255, y = 394)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 320, y = 398, height = 25, width = 100)
    lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
    lbl.place(x = 420, y = 405)

    lbl = Label(window, text = "ALT = ", font = ("Times New Roman", 16))
    lbl.place(x = 505, y = 394)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 570, y = 398, height = 25, width = 100)
    lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
    lbl.place(x = 670, y = 405)

    lbl = Label(window, text = "ALP = ", font = ("Times New Roman", 16))
    lbl.place(x = 775, y = 394)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 840, y = 398, height = 25, width = 100)
    lbl = Label(window, text = " IU/L", font = ("Open Sans",10))
    lbl.place(x = 940, y = 405)

window = Tk()
window.resizable(0,0)
gui(window)

Btn = Button(window, text ="Submit", bd = 6, font = ("Open Sans", 16))
Btn.pack()
Btn.place(x = 380, y = 460, height = 50, width = 100)

Btn = Button(window, text ="Reset", bd = 6, font = ("Open Sans", 16))
Btn.pack()
Btn.place(x = 580, y = 460, height = 50, width = 100)

window.title("Patient Medical Report")
window.geometry("1050x550")
window.mainloop()
