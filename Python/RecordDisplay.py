from tkinter import *
from tkinter import messagebox
import mysql as my
from mysql import connector

mydb = mysql.connector.connect(host = "127.0.0.1", user = root)
root = Tk()
root.title("Patient Medical Report")
root.geometry("500x550")
root.mainloop()