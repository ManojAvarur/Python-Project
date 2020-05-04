from tkinter import *
import os

def callBack():
    filename = "MedicalManagement.py"
    os.system(filename)

root = Tk()
root.resizable(0,0)
btn = Button(root, text = "Insert New Patient Details", bd = 6, font = ("Open Sans", 16), command = callBack)
btn.pack()
root.title("Patient Medical Report")
root.geometry("1050x550")
root.mainloop()
