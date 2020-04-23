from tkinter import *
from random import randint as ri

def genRandInt():
    return ri(1000,10000)

def bloodGroup(window):
    bloodGroups = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    variable = StringVar(window)
    variable.set("Select Blood Group")
    w = OptionMenu(window, variable, *bloodGroups)
    w.config(font = ("Times New Roman", 16))
    w.pack()
    w.place(x = 720, y = 157, height = 28, width = 200)


def gui(window):

    # ---------------------- Heading ---------------------------------------
    lbl = Label(window, text = "Enter Patient Details",font = ("Times New Roman", 26))
    lbl.place(x = 350, y = 10)
    lbl = Label(window, text = "----------------------------------",font = ("Times New Roman", 26))
    lbl.place(x = 305, y = 50, height = 25)

    # ---------------------- First Row ---------------------------------------
    lbl = Label(window, text = "Patient ID : ", font = ("Times New Roman", 20))
    lbl.place(x = 32, y = 90)
    txtfld = Entry(window, bd = 1.5,  font = ("Times New Roman", 16))
    txtfld.insert(0,genRandInt())
    txtfld.config(state = 'disabled')
    txtfld.place(x = 170, y = 98, height = 25, width = 200)

    lbl = Label(window, text = "Name : ", font = ("Times New Roman", 20))
    lbl.place(x = 630, y = 90)
    txtfld = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld.place(x = 720, y = 98, height = 25, width = 200)

    # ---------------------- Second Row ---------------------------------------
    lbl = Label(window, text = "Phone No : ", font = ("Times New Roman", 20))
    lbl.place(x = 35, y = 150)
    txtfld1 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld1.place(x = 170, y = 158, height = 25, width = 200)

    lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
    lbl.place(x = 550, y = 150)
    # txtfld2 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    # txtfld2.place(x = 720, y = 158, height = 25, width = 200)
    bloodGroup(window)

    # ---------------------- Third Row ----------------------------------------
    lbl = Label(window, text = "Sugar Level : ", font = ("Times New Roman", 20))
    lbl.place(x = 15, y = 210)
    txtfld3 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld3.place(x = 170, y = 218, height = 25, width = 200)

    lbl = Label(window, text = "Blood Pressure : ", font = ("Times New Roman", 20))
    lbl.place(x = 528, y = 210)
    txtfld4 = Entry(window, bd = 1.5, font = ("Times New Roman", 16))
    txtfld4.place(x = 720, y = 218, height = 25, width = 200)


window = Tk()
window.resizable(0,0)
gui(window)
window.title('Patient Medical Report')
window.geometry("1000x700")
window.mainloop()
