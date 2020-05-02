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

# ---------------------- Heading Row ---------------------------------------
    lbl = Label(window, text = "Enter Patient Details",font = ("Times New Roman", 26))
    lbl.place(x = 385, y = 10)
    lbl = Label(window, text = "----------------------------------",font = ("Times New Roman", 26))
    lbl.place(x = 340, y = 50, height = 25)

# ---------------------- First Row ---------------------------------------
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

# ---------------------- Second Row ---------------------------------------
    lbl = Label(window, text = "Phone No : ", font = ("Times New Roman", 20))
    lbl.place(x = 105, y = 150)
    txtfld_2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_2.place(x = 240, y = 158, height = 25, width = 200)

    lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
    lbl.place(x = 620, y = 150)
    # txtfld2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    # txtfld2.place(x = 720, y = 158, height = 25, width = 200)
    bloodGroup( window )

# ---------------------- Third Row (Sugar Tests) ----------------------------------------
    lbl = Label(window, text = "FBC : ", font = ("Times New Roman", 20))
    lbl.place(x = 165, y = 210)
    txtfld_3 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_3.place(x = 240, y = 218, height = 25, width = 200)

    lbl = Label(window, text = "PPBS : ", font = ("Times New Roman", 20))
    lbl.place(x = 700, y = 210)
    txtfld_4 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_4.place(x = 790, y = 218, height = 25, width = 200)

# ---------------------- Forth Row ----------------------------------------
    lbl = Label(window, text = "Hypertension (BP) : ", font = ("Times New Roman", 20))
    lbl.place(x = 12, y = 270)
    txtfld_5 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_5.place(x = 240, y = 278, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 588, y = 270)
    txtfld_6 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_6.place(x = 790, y = 278, height = 25, width = 200)

# ---------------------- Fifth Row ----------------------------------------
    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 42, y = 330)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 240, y = 338, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 568, y = 330)
    txtfld_8 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_8.place(x = 790, y = 338, height = 25, width = 200)
    
# ---------------------- Sixth Row ----------------------------------------
    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 62, y = 390)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 240, y = 398, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 588, y = 390)
    txtfld_8 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_8.place(x = 790, y = 398, height = 25, width = 200)


window = Tk()
window.resizable(0,0)
gui(window)
window.title("Patient Medical Report")
window.geometry("1050x700")
window.mainloop()
