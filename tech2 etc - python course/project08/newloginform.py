from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #Background image
        self.bg=ImageTk.PhotoImage(file="moon.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #title frame
        frame=Frame(self.root, bg="cyan")
        frame.place(x=300, y=150, width=500, height=400)

        #title and subtitle

        title = Label(frame, text="Login Form", font=("Impact", 35,"bold"), fg="#6162FF", bg="cyan").place(x=90, y=30)
        subtitle = Label(frame, text="Member Login area", font=("Goudy old style", 15,"bold"), fg="#1d1d1d", bg="cyan").place(x=90, y=100)

        #username
        username = Label(frame, text="username", font=("Goudy old style", 15,"bold"), fg="grey", bg="cyan").place(x=90, y=140)
        self.username=Entry(frame, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90,y=170, width=320,height=35)

        #password
        password = Label(frame, text="password", font=("Goudy old style", 15,"bold"), fg="grey", bg="cyan").place(x=90, y=210)
        self.password=Entry(frame, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90,y=240, width=320,height=35)

        #forgot and submit button
        forgot=Button(frame, text="forgot password?",bd=0,cursor="hand2",font=("Goudy old style",12),fg="#6162FF", bg="white").place(x=90,y=280)
        submit=Button(frame, text="Login",command=self.check_fun,cursor="hand2",bd=0,font=("Goudy old style",15),bg="#6162FF", fg="white").place(x=90,y=320, width=180, height=40)

    def check_fun(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields need to be filled",parent=self.root)
            elif self.username.get()!="iamjas6" or self.password.get()!="Syedsuhail@786":
                messagebox.showerror("Error","Incorrect username or password",parent=self.root)
            else:
                messagebox.showinfo("Welcome",f"Welcome {self.username.get()}")




root = Tk()
obj=Login(root)
root.mainloop()