# from tkinter import *


# class MyWindow:
#     def __init__(self, win):
#         self.lbl1 = Label(win, text='First number')
#         self.lbl2 = Label(win, text='Second number')
#         self.lbl3 = Label(win, text='Result')
#         self.t1 = Entry(bd=3)
#         self.t2 = Entry()
#         self.t3 = Entry()
#         self.btn1 = Button(win, text='Add')
#         self.btn2 = Button(win, text='Subtract')
#         self.lbl1.place(x=100, y=50)
#         self.t1.place(x=200, y=50)
#         self.lbl2.place(x=100, y=100)
#         self.t2.place(x=200, y=100)
#         self.b1 = Button(win, text='Add', command=self.add)
#         self.b2 = Button(win, text='Subtract')
#         self.b2.bind('<Button-1>', self.sub)
#         self.b1.place(x=100, y=150)
#         self.b2.place(x=200, y=150)
#         self.lbl3.place(x=100, y=200)
#         self.t3.place(x=200, y=200)

#     def add(self):
#         self.t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1+num2
#         self.t3.insert(END, str(result))

#     def sub(self, event):
#         self.t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1-num2
#         self.t3.insert(END, str(result))


# window = Tk()
# MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------

import tkinter  as tk

root=tk.Tk()


canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

# username = tk.Entry(root)
# canvas1.create_window(200,140, window=username)
# canvas1.create_text(100,140,fill="darkblue",text="username")

# password = tk.Entry(root)
# canvas1.create_window(200,180,window=password)
# canvas1.create_text(100,180,fill="darkblue",text="password")

variable = tk.StringVar(canvas1)
variable.set("Facebook")

w=tk.OptionMenu(root , variable, "Facebook","Twitter","Spotify","Swiggy")
w.pack()

# button1= tk.Button(text='Go')
# canvas1.create_window(250,250, window=button1)

root.mainloop()