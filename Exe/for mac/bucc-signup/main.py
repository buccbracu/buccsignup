from tkinter import *
import time
from PIL import Image, ImageTk
import os
from database import query



class Signup:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("BUCC Signup Form")

        self.window_width = self.master.winfo_screenwidth()
        self.window_height = self.master.winfo_screenheight()
        self.master.geometry("750x%d" % (self.window_height-200))

        #Loading Right Background
        open = Image.open("images/background.png")
        open = open.resize((200, (self.window_height - 200)), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=550, y=0)

        #Loading Left Background
        openl = Image.open("images/back-l.jpg")
        imagel = ImageTk.PhotoImage(openl)
        self.imgl = Label(self.master, image=imagel, borderwidth=0, bg="#EAF0F1")
        self.imgl.image = imagel
        self.imgl.place(x=-130, y=0)

        # #Loading BUCC image
        # open = Image.open("images/backbucc.jpg")
        # open = open.resize((200,200), Image.ANTIALIAS)
        # image = ImageTk.PhotoImage(open)
        # img = Label(master, image=image, borderwidth=0)
        # img.image = image
        # img.place(x=50, y=15)

        #Loading BUCC Full Name image
        open = Image.open("images/BUCC.png")
        # open = open.resize((200,200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=250, y=5)

        #Loading signup image
        open = Image.open("images/recruit.png")

        open = open.resize((150,20), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=420, y=50)

        #Loading signuplogo image
        open = Image.open("images/signup-logo.jpg")
        open = open.resize((100,100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=440, y=80)

        #Creating Name label
        labelN = Label(self.master, text="Name:", font=("Times", 16), bg="#EAF0F1")
        labelN.place(x=340, y=200)

        #Taking Name Input
        self.name =StringVar()
        inputN = Entry(self.master,font=("Times", 16, "italic"), justify="center",width=30, textvariable=self.name)
        inputN.place(x=340, y=230)


        #Creating ID label
        labelN = Label(self.master, text="Student ID:", font=("serif", 16), bg="#EAF0F1")
        labelN.place(x=340, y=280)

        #Taking ID Input
        self.id =StringVar()
        inputN = Entry(self.master,font=("Times", 16, "italic"), justify="center",width=30, textvariable=self.id)
        inputN.place(x=340, y=310)

        #Creating Email label
        labelN = Label(self.master, text="Email:", font=("serif", 16), bg="#EAF0F1")
        labelN.place(x=340, y=360)

        #Taking Email Input
        self.email = StringVar()
        inputN = Entry(self.master,font=("Times", 16, "italic"), justify="center",width=30, textvariable=self.email)
        inputN.place(x=340, y=390)

        #Creating Phone no label
        labelN = Label(self.master, text="Mobile No:", font=("Times", 16, "italic"), bg="#EAF0F1")
        labelN.place(x=340, y=440)

        #Taking Phone no Input
        self.number = StringVar()
        inputN = Entry(self.master,font=("baskerville", 14, "italic"), justify="center",width=30, textvariable=self.number)
        inputN.place(x=340, y=470)

        #Button
        btn = Button(self.master, text="Submit", font=("serif", 10, "bold"), activebackground="#3498DB", activeforeground="#758AA2", width=10, command=self.submit)
        btn.image = image
        btn.place(x=450, y=520)




    def submit(self):
        if (self.name.get() == "") or (self.id.get() == "") or (self.email.get() == "") or (self.number.get() == ""):
            openl = Image.open("images/back-wr.jpg")
            imagel = ImageTk.PhotoImage(openl)
            self.imgl = Label(self.master, image=imagel, borderwidth=0, bg="#EAF0F1")
            self.imgl.image = imagel
            self.imgl.place(x=-130, y=0)
            print("All Fields are not Covered")
        else:
            openl = Image.open("images/back-c.jpg")
            imagel = ImageTk.PhotoImage(openl)
            self.imgl = Label(self.master, image=imagel, borderwidth=0, bg="#EAF0F1")
            self.imgl.image = imagel
            self.imgl.place(x=-130, y=0)
            input = (self.name.get(), self.id.get(), self.email.get(), self.number.get())
            query(input)
            print(self.name.get() + " " + self.id.get() + self.email.get() + " " + self.number.get())



def main():
    root = Tk()
    app = Signup(root)
    root.configure(background="#EAF0F1")
    root.mainloop()

if __name__ == '__main__':
    main()
