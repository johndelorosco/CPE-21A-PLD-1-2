from tkinter import *
win = Tk()

#add widgets
class MyWin:
    def __init__(self,win):
        self.lbl1 = Label(win, text="My First Standard Calculator")
        self.lbl1.place(x=200, y=20)
        self.lbl2 = Label(win, text="1st no.")
        self.lbl2.place(x=100, y=50)
        self.txt1 = Entry(win, bd=2)
        self.txt1.place(x=150, y=50)
        self.lbl3 = Label(win, text="2nd no.")
        self.lbl3.place(x=100, y=80)
        self.txt2 = Entry(win, bd=2)
        self.txt2.place(x=150, y=80)
        self.lbl4 = Label(win, text="Result")
        self.lbl4.place(x=100, y=120)
        self.txt3 = Entry(win, bd=2)
        self.txt3.place(x=150, y=120)
        self.btn1 = Button(win, text="Addition", height= 1, width= 11)
        self.btn1.bind('<Button-1>', self.addition)
        self.btn1.place(x=100, y=150)
        self.btn2 = Button(win, text="Subtraction", height= 1, width= 11)
        self.btn2.bind('<Button-1>', self.subtraction)
        self.btn2.place(x=190, y=150)
        self.btn3 = Button(win, text="Multiplication", height= 1, width= 11)
        self.btn3.bind('<Button-1>', self.multiplication)
        self.btn3.place(x=280, y=150)
        self.btn4 = Button(win, text="Division", height= 1, width= 11)
        self.btn4.bind('<Button-1>', self.division)
        self.btn4.place(x=370, y=150)
        self.btn5 = Button(win, text="Clear", height= 1, width= 11)
        self.btn5.bind('<Button-1>', self.clear)
        self.btn5.place(x=200, y=200)
    def addition(self,event):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def subtraction(self,event):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def multiplication(self,event):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def division(self,event):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

    def clear(self,event):
        self.txt3.delete(0,'end')

mywin = MyWin(win)


win.geometry("500x400+10+10")
win.title("Standard Calculator")
win.mainloop()
