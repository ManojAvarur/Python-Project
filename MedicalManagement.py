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
    w.place(x = 740, y = 157, height = 28, width = 200)


def gui( window ):

# ---------------------- Heading Row ---------------------------------------
    lbl = Label(window, text = "Enter Patient Details",font = ("Times New Roman", 26))
    lbl.place(x = 350, y = 10)
    lbl = Label(window, text = "----------------------------------",font = ("Times New Roman", 26))
    lbl.place(x = 305, y = 50, height = 25)

# ---------------------- First Row ---------------------------------------
    lbl = Label(window, text = "Patient ID : ", font = ("Times New Roman", 20))
    lbl.place(x = 52, y = 90)
    txtfld_0 = Entry(window, bd = 1.5,  font = ("Times New Roman", 16))
    txtfld_0.insert(0,genRandInt())
    txtfld_0.config(state = 'disabled')
    txtfld_0.place(x = 190, y = 98, height = 25, width = 200)

    lbl = Label(window, text = "Name : ", font = ("Times New Roman", 20))
    lbl.place(x = 650, y = 90)
    txtfld_1 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_1.place(x = 740, y = 98, height = 25, width = 200)

# ---------------------- Second Row ---------------------------------------
    lbl = Label(window, text = "Phone No : ", font = ("Times New Roman", 20))
    lbl.place(x = 55, y = 150)
    txtfld_2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_2.place(x = 190, y = 158, height = 25, width = 200)

    lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
    lbl.place(x = 570, y = 150)
    # txtfld2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    # txtfld2.place(x = 720, y = 158, height = 25, width = 200)
    bloodGroup( window )

# ---------------------- Third Row ----------------------------------------
    lbl = Label(window, text = "Sugar Level : ", font = ("Times New Roman", 20))
    lbl.place(x = 35, y = 210)
    txtfld_3 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_3.place(x = 190, y = 218, height = 25, width = 200)

    lbl = Label(window, text = "Blood Pressure : ", font = ("Times New Roman", 20))
    lbl.place(x = 548, y = 210)
    txtfld_4 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_4.place(x = 740, y = 218, height = 25, width = 200)

# ---------------------- Forth Row ----------------------------------------
    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 22, y = 270)
    txtfld_5 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_5.place(x = 190, y = 278, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 548, y = 270)
    txtfld_6 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_6.place(x = 740, y = 278, height = 25, width = 200)

# ---------------------- Fifth Row ----------------------------------------
    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 22, y = 330)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 190, y = 338, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 548, y = 330)
    txtfld_8 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_8.place(x = 740, y = 338, height = 25, width = 200)
    
# ---------------------- Sixth Row ----------------------------------------
    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 22, y = 390)
    txtfld_7 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_7.place(x = 190, y = 398, height = 25, width = 200)

    lbl = Label(window, text = "Disease Type : ", font = ("Times New Roman", 20))
    lbl.place(x = 548, y = 390)
    txtfld_8 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld_8.place(x = 740, y = 398, height = 25, width = 200)


window = Tk()
window.resizable(0,0)
gui(window)
window.title("Patient Medical Report")
window.geometry("1000x700")
window.mainloop()
