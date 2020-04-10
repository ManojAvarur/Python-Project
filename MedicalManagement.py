from tkinter import *


def gui():

    lbl = Label(window, text="Enter Patient Details",font = ("Times New Roman", 26))
    lbl.place(x = 350, y = 10)
    lbl = Label(window, text="----------------------------------",font = ("Times New Roman", 26))
    lbl.place(x = 305, y = 50, height = 25)

    lbl = Label(window, text = "Name : ", font = ("Times New Roman", 20))
    lbl.place(x = 80, y = 90)
    txtfld = Entry(window, bd = 1.5)
    txtfld.place(x = 170, y = 98, height = 25, width = 200)

    lbl = Label(window, text = "Blood Group : ", font = ("Times New Roman", 20))
    lbl.place(x = 550, y = 90)
    txtfld1 = Entry(window, bd = 1.5)
    txtfld1.place(x = 720, y = 98, height = 25, width = 200)


window = Tk()
gui()
window.title('Patient Medical Report')
window.geometry("1000x700")
window.mainloop()
