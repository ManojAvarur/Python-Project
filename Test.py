from tkinter import *
class All:
    def __init__(self, x):
        self.win = x
        self.t1 = Entry(bd=3)
        self.t1.place(x=150,y=150)
        # self.t2 = Entry(bd=3)
        # self.t2.place(x=200,y=200)
        self.b1 = Button(self.win, text='Show', command=self.clear)
        self.b1.pack()


    def clear(self):
        lbl = Label(self.win, text = str(self.t1.get()) ,font = ("Times New Roman", 26))
        lbl.place(x=250,y=250)
        self.t1.delete(0, 'end')
        self.t1.insert(END, "")
        
        #     def add(self):
#         self.t3.delete(0, 'end')
#         num1 = int(self.t1.get())
#         num2 = int(self.t2.get())
#         result = num1+num2
#         self.t3.insert(END, str(result))



    # def add(self,win):
    #     t1 = Entry(bd=3)
    #     t1.place(x=150,y=150)
    #     b1 = Button(win, text='Show', command=clear(win))




window = Tk()
All(window)
# ubj.add(window)
window.title('Hello Python')
window.geometry("1000x1000")
window.mainloop()










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