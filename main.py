# import package GUI
from tkinter import *
from PIL import ImageTk , Image
#____________________________ALL GUI CODE____________________________

# ____________________________sign up GUI CODE____________________________
def Signup():
    # --------------------------------------------------------------------
    # variable class Tk from tkinter lib
    window_SignUP = Tk()
    # --------------------------------------------------------------------
    # customize windows app
    window_SignUP.title("Passam(Sign Up)")
    window_SignUP.config(bg="#353535")
    window_SignUP.geometry("800x500")
    window_SignUP.resizable(False,False)
    window_SignUP.iconbitmap("iconApp.ico")
    # --------------------------------------------------------------------
    # image icon app in window
    Passam_Image_Icon = Image.open("logo.jpg")
    Passam_Image_Icon = Passam_Image_Icon.resize((320,210))
    Tk_Passam_Image = ImageTk.PhotoImage(Passam_Image_Icon)
    Passam_Image__Label = Label(window_SignUP,image=Tk_Passam_Image)
    Passam_Image__Label.place(x=50,y=140)
    # --------------------------------------------------------------------
    # text welcome in app header
    Text_Welcome = Label(window_SignUP,text="Welcome",bg="#353535",fg="white",width=10)
    Text_Welcome.pack()
    Text_Welcome.place(x=220,y=20)
    Text_Welcome_style = ("Caveat" , 50)
    Text_Welcome.configure(font=Text_Welcome_style)
    # --------------------------------------------------------------------
    # text enter password
    Text_Enter_Password = Label(window_SignUP,text="Enter your password for sign up",bg="#353535",fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=420,y=150)
    Text_Password_style = ("Comic Sans Ms" , 15 ,"bold")
    Text_Enter_Password.configure(font=Text_Password_style)
    # --------------------------------------------------------------------
    # edit text enter password
    Password_Entry=Entry(window_SignUP,width=42)
    Password_Entry.pack()
    Password_Entry.place(x=395,y=220)
    Password_Entry_style=("Arial")
    Password_Entry.configure(font=Password_Entry_style)
    # --------------------------------------------------------------------
    # button sign up
    Button_SignUp=Button(window_SignUP,text="Sign Up",width=20,bg="green",fg="white")
    Button_SignUp.pack()
    Button_SignUp.place(x=450,y=280)
    Button_SignUp_style=("Cenataur",17,"bold")
    Button_SignUp.configure(font=Button_SignUp_style)
    window_SignUP.mainloop()
# ____________________________End sign up GUI CODE____________________________

Signup()

