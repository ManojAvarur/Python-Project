from tkinter import *



def prt():
    print(variable.get())

window = Tk()
window.resizable(0,0)
bloodGroups = ["A+","A-","B+","B-","O+","O-","AB+","AB-"]
variable = StringVar(window)
variable.set("Select Blood Group")
w = OptionMenu(window, variable, *bloodGroups)
w.config(font = ("Times New Roman", 16))
w.pack()

Btn = Button(window, text ="Submit", bd = 6, font = ("Open Sans", 16), command = prt)
Btn.pack()
Btn.place(x = 380, y = 460, height = 50, width = 100)

window.title("Patient Medical Report")
window.geometry("1050x550")
window.mainloop()

# w.place(x = 790, y = 157, height = 28, width = 200)

















import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Patient-ID could not be generated please contact the developer")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")


#---------------------------------------------------------------------------------------------------------------------------------------------------


# from tkinter import *
# class All:
#     def __init__(self, x):
# win = x
# t1 = Entry(bd=3)
# t1.place(x=150,y=150)
#         # self.t2 = Entry(bd=3)
#         # self.t2.place(x=200,y=200)
# b1 = Button(self.win, text='Show', command=self.clear)
# b1.pack()


#     def clear(self):
#         lbl = Label(self.win, text = str(self.t1.get()) ,font = ("Times New Roman", 26))
#         lbl.place(x=250,y=250)
# t1.delete(0, 'end')
# t1.insert(END, "")


# window = Tk()
# All(window)
# # ubj.add(window)
# window.title('Hello Python')
# window.geometry("1000x1000")
# window.mainloop()





#---------------------------------------------------------------------------------------------------------------------------------------------------




# from tkinter import *


# class MyWindow:
#     def __init__(self, win):
# lbl1 = Label(win, text='First number')
# lbl2 = Label(win, text='Second number')
# lbl3 = Label(win, text='Result')
# t1 = Entry(bd=3)
# t2 = Entry()
# t3 = Entry()
# btn1 = Button(win, text='Add')
# btn2 = Button(win, text='Subtract')
# lbl1.place(x=100, y=50)
# t1.place(x=200, y=50)
# lbl2.place(x=100, y=100)
# t2.place(x=200, y=100)
# b1 = Button(win, text='Add', command=self.add)
# b2 = Button(win, text='Subtract')
# b2.bind('<Button-1>', self.sub)
# b1.place(x=100, y=150)
# b2.place(x=200, y=150)
# lbl3.place(x=100, y=200)
# t3.place(x=200, y=200)

#     def add(self):
# t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1+num2
# t3.insert(END, str(result))

#     def sub(self, event):
# t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1-num2
# t3.insert(END, str(result))


# window = Tk()
# MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------

# import tkinter  as tk

# root=tk.Tk()


# canvas1 = tk.Canvas(root, width = 400, height = 300)
# canvas1.pack()

# # username = tk.Entry(root)
# # canvas1.create_window(200,140, window=username)
# # canvas1.create_text(100,140,fill="darkblue",text="username")

# # password = tk.Entry(root)
# # canvas1.create_window(200,180,window=password)
# # canvas1.create_text(100,180,fill="darkblue",text="password")

# variable = tk.StringVar(canvas1)
# variable.set("Facebook")

# w=tk.OptionMenu(root , variable, "Facebook","Twitter","Spotify","Swiggy")
# w.pack()

# button1= tk.Button(text='Go')
# canvas1.create_window(250,250, window=button1)

# root.mainloop()