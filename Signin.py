from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

row = ""

def login_user():

    global row

    if usernameEntry.get()=='' or passwordEntry.get()== '':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not estaplished try again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password= %s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()

        if row == None:
            messagebox.showerror('Error','Invalid username Or password')

        else:
            messagebox.showinfo('Welcome','login is sucessful')
            login_window.destroy()
        
            import Menu_Cal
        


def signup_page():
    login_window.destroy()
    import register_GUI

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='img/cl.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='img/op.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

login_window = Tk()
login_window.geometry('1280x720')
login_window.resizable(0,0)
bgImage = ImageTk.PhotoImage(file='img/bg2.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0) 
login_window.title("Sign in")

heading = Label(login_window,text='USER LOGIN',font=('Fc SaveSpace',50,'bold'),bg='white',fg='gray1')
heading.place(x=600,y=150) # center heading

usernameEntry = Entry(login_window,width=15,font=('Fc SaveSpace',43),bg='white',fg='gray1')
usernameEntry.place(x=570,y=250)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=260,height=4,bg='gold').place(x=570,y=300)

passwordEntry = Entry(login_window,width=15,font=('Fc SaveSpace',43),bg='white',fg='gray1')
passwordEntry.place(x=570,y=330)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=260,height=4,bg='gold').place(x=570,y=380)

openeye = PhotoImage(file='img/cl.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=850,y=335)

loginButton = Button(login_window,text='Login' , font=('Fc SaveSpace',30,'bold'),fg='white',bg='gray1',activeforeground='white',activebackground='gray1'
                        ,cursor='hand2',bd=0,width=22,command=login_user)
loginButton.place(x=565,y=400)

signupLabel = Label(login_window,text="Don't have an account?",font=('Fc SaveSpace',33),bg='white',fg='gray1')
signupLabel.place(x=500,y=500)

NewButton = Button(login_window,text='Create new one',font=('Fc SaveSpace',33,'underline'),bg='white',fg='gold',bd=0,activeforeground='blue'
                ,activebackground='white',cursor='hand2',command=signup_page)
NewButton.place(x=740,y=490)


login_window.mainloop()
