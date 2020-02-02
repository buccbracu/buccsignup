from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from openpyxl import Workbook
import re



class Signup:
    def __init__(self, master):
        #creating or loading xlx file
        self.fname = ''
        self.wb = Workbook()
        self.sheet = self.wb.active
        #setting text color of title
        self.sheet.append(("Name", "Id", "Email", "Number"))

        self.master = master
        self.frame = Frame(self.master)
        self.master.title("BUCC Signup Form")

        self.window_width = self.master.winfo_screenwidth()
        self.window_height = self.master.winfo_screenheight()
        self.master.geometry("500x590")

        #arrows and mouse button-1
        self.master.bind('<Button-1>', self.button_1)
        self.master.bind('<Down>', self.downKey)
        self.master.bind('<Up>', self.upKey)
        self.focused_entry = 0

        #Loading Right Background
        open = Image.open("images/background.png")
        open = open.resize((200, (self.window_height - 150)), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=300, y=10)

        #Loading BUCC Full Name image
        open = Image.open("images/ClubLogo.png")
        open = open.resize((260, 60), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=120, y=20)


        #Loading signuplogo image
        open = Image.open("images/signup-logo.jpg")
        open = open.resize((80, 80), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(open)
        img = Label(self.master, image=image, borderwidth=0, bg="#EAF0F1")
        img.image = image
        img.place(x=200, y=100)

        #Creating Name label
        self.labelN = Label(self.master, text="Name:", font=("Times", 16), bg="#EAF0F1")
        self.labelN.place(x=90, y=200)

        #Taking Name Input
        self.name =StringVar()
        self.inputN = Entry(self.master,font=("Times", 16), justify="center",width=30, textvariable=self.name)
        self.inputN.place(x=90, y=230)


        #Creating ID label
        self.labelI = Label(self.master, text="Student ID:", font=("Times", 16), bg="#EAF0F1")
        self.labelI.place(x=90, y=280)

        #Taking ID Input
        self.id =StringVar()
        self.inputI = Entry(self.master,font=("Times", 16), justify="center",width=30, textvariable=self.id)
        self.inputI.place(x=90, y=310)

        #Creating Email label
        self.labelE = Label(self.master, text="Email:", font=("Times", 16), bg="#EAF0F1")
        self.labelE.place(x=90, y=360)

        #Taking Email Input
        self.email = StringVar()
        self.inputE = Entry(self.master,font=("Times", 16), justify="center",width=30, textvariable=self.email)
        self.inputE.place(x=90, y=390)

        #Creating Phone no label
        self.labelP = Label(self.master, text="Mobile No:", font=("Times", 16), bg="#EAF0F1")
        self.labelP.place(x=90, y=440)

        #Taking Phone no Input
        self.number = StringVar()
        self.inputP = Entry(self.master, font=("Times", 16), justify="center", width=30, textvariable=self.number)
        self.inputP.place(x=90, y=470)

        #Submit Button
        btn = Button(self.master, text="Submit", font=("serif", 10, "bold"), activebackground="#3498DB", activeforeground="#758AA2", width=10, command=self.submit)
        btn.image = image
        btn.place(x=200, y=520)
        self.popup_success()



    #checks the values and pass them for xlsx entry
    def submit(self):
        name_regex = '^[A-Za-z_\s]+$'
        id_number_regex = '^[0-9]+$'
        email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(name_regex, self.name.get())):
            if(re.search(id_number_regex, self.id.get())):
                if(re.search(email_regex, self.email.get())):
                    if(re.search(id_number_regex, self.number.get())):
                        #writing values into worksheet
                        self.sheet.append((self.name.get(), self.id.get(), self.email.get(), self.number.get()))
                        if (self.fname == ''):
                            if(self.fname_sv.get() == ''):
                                self.fname = "ExelFiles/buccsignup.xlsx"
                            else:
                                self.fname = "ExelFiles/" + self.fname_sv.get() + ".xlsx"
                        try:
                            self.wb.save(self.fname)
                        except FileNotFoundError:
                            os.mkdir('ExelFiles')
                            self.wb.save(self.fname)

                        #deleting all values from entry box
                        self.inputN.delete('0', END)
                        self.inputI.delete('0', END)
                        self.inputE.delete('0', END)
                        self.inputP.delete('0', END)
                        messagebox.showinfo(title="Awsome", message="Thankyou\n For further informaion\n check your email")
                    else:
                        messagebox.showwarning(title="Invalid", message="Phone number can only contain digits (0-9)")
                        self.inputP.delete('0', END)
                        self.inputP.focus()
                        self.focused_entry = 4
                else:
                    messagebox.showwarning(title="Invalid", message="Email consists of an email prefix and an email domain\
                    \n  Example: bucc@gmail.com")
                    self.inputE.delete('0', END)
                    self.inputE.focus()
                    self.focused_entry = 3
            else:
                messagebox.showwarning(title="Invalid", message="Id can only contain digits (0-9)\n  Example: 17101120")
                self.inputI.delete('0', END)
                self.inputI.focus()
                self.focused_entry = 2
        else:
            messagebox.showwarning(title="Invalid", message="Name can only contain letters (a-z)\n  Example: Mushfiq")
            self.inputN.delete('0', END)
            self.inputN.focus()
            self.focused_entry = 1

    #popup for exel file name
    def popup_success(self):
        fname = Toplevel(bg="#EAF0F1")
        fname.geometry("300x150+240+350")
        fname.title("Set File Name")
        #Creating Name label
        labelF = Label(fname, text="Write file name", font=("Times", 16), bg="#EAF0F1")
        labelF.place(x=90, y=30)

        #Taking Name Input
        self.fname_sv = StringVar()
        inputF = Entry(fname, font=("Times", 16), justify="center", width=20, textvariable=self.fname_sv)
        inputF.place(x=40, y=70)

        #Submit Button
        fbtn = Button(fname, text="Submit", font=("serif", 10, "bold"), activeforeground="#758AA2", width=10, command=fname.destroy)
        fbtn.place(x=110, y=110)
        def y(self):
            print(self.fname)

    # controlling mouse left button
    def button_1(self, event):
        self.frame.focus_set()
        if (str(self.frame.focus_get())) == ".!entry":
            self.focused_entry = 1
        elif (str(self.frame.focus_get())) == ".!entry2":
            self.focused_entry = 2
        elif (str(self.frame.focus_get())) == ".!entry3":
            self.focused_entry = 3
        else:
            self.focused_entry = 4

    # controlling down key
    def downKey(self, event):
        if (self.focused_entry) == 1:
            self.inputI.focus()
            self.focused_entry = 2
        elif (self.focused_entry) == 2:
            self.inputE.focus()
            self.focused_entry = 3
        elif (self.focused_entry) == 3:
            self.inputP.focus()
            self.focused_entry = 4

    # controlling up key
    def upKey(self, event):
        if (self.focused_entry) == 4:
            self.inputE.focus()
            self.focused_entry = 3
        elif (self.focused_entry) == 2:
            self.inputN.focus()
            self.focused_entry = 1
        elif (self.focused_entry) == 3:
            self.inputI.focus()
            self.focused_entry = 2



def main():
    root = Tk()
    root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='images/BUCC-logo.png'))
    app = Signup(root)
    root.configure(background="#EAF0F1")
    root.mainloop()

if __name__ == '__main__':
    main()
