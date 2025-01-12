from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if userEntry.get()=='' or passwordEntry.get()==''or confirmEntry.get()=='' or emailEntry.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Condtions')
    else:
        try:
            con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'Create table data(id int auto_increment key not null ,email varchar(50) ,username varchar(100) ,password varchar(20), fname varchar(40), lname varchar(40))'
            mycursor.execute(query)
            
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username = %s'
        mycursor.execute(query,(userEntry.get()))

        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already exists')

        else:
            query = 'insert into data(email,username,password,fname,lname) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),userEntry.get(),passwordEntry.get(),firstEntry.get(),lastEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import Signin
    

def login_page():
    signup_window.destroy()
    import Signin

signup_window = Tk()
signup_window.geometry('1280x720')
signup_window.resizable(False,False)
bgImage = ImageTk.PhotoImage(file='img/bg2.jpg')
signup_window.title("Register")

bgLabel = Label(signup_window,image=bgImage)
bgLabel.grid()

frames = Frame(signup_window)
frames.place(x=540,y=30)


heading = Label(frames,text='CREATE AN ACCOUNT',font=('Fc SaveSpace',40),fg='gray1')
heading.grid(row=0,column=0,padx=10,pady=10) # center heading

# Username
userLabel = Label(frames,text='Username',font = ('Fc SaveSpace',25),fg='gray1')
userLabel.grid(row=1,column=0,sticky='w',padx=5)
userEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
userEntry.grid(row=2,column=0,sticky='w',padx=5)

# Password
passwordLabel = Label(frames,text='Password',font = ('Fc SaveSpace',25),fg='gray1')
passwordLabel.grid(row=3,column=0,sticky='w',padx=5)
passwordEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
passwordEntry.grid(row=4,column=0,sticky='w',padx=5)

# Confirm password
confirmLabel = Label(frames,text='Confirm Password',font = ('Fc SaveSpace',25),fg='gray1')
confirmLabel.grid(row=5,column=0,sticky='w',padx=5)
confirmEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
confirmEntry.grid(row=6,column=0,sticky='w',padx=5)

# First Name
firstLabel = Label(frames,text='First Name',font = ('Fc SaveSpace',25),fg='gray1')
firstLabel.grid(row=7,column=0,sticky='w',padx=5)
firstEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
firstEntry.grid(row=8,column=0,sticky='w',padx=5)

# Last name

lastLabel = Label(frames,text='Last Name',font = ('Fc SaveSpace',25),fg='gray1')
lastLabel.grid(row=9,column=0,sticky='w',padx=5)
lastEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
lastEntry.grid(row=10,column=0,sticky='w',padx=5)

# Email
emailLabel = Label(frames,text='Email',font = ('Fc SaveSpace',25),fg='gray1')
emailLabel.grid(row=11,column=0,sticky='w',padx=5)
emailEntry = Entry(frames,width=30,font=('Fc SaveSpace',25),fg='gold',bg='gray1')
emailEntry.grid(row=12,column=0,sticky='w',padx=5)

check = IntVar()

# terms and con
termsandconditions = Checkbutton(frames,text='I agree to the Terms & Conditions',font=('Fc SaveSpace',22),fg='red',bg='gray1'
                    ,activebackground='white',activeforeground='gold',cursor='hand2',variable=check)
termsandconditions.grid(row=13,column=0,pady=10)

# Button
signupButton = Button(frames,text='SignUp',font=('Fc SaveSpace',25),bd=0,fg='white',bg='gray1',width=34,command=connect_database)
signupButton.grid(row=14,column=0)

# alreadyaccount
alreadyaccount = Label(frames,text="Don't have an account ? ",font=('Fc SaveSpace',25))
alreadyaccount.grid(row=15,column=0,sticky='w',padx=5)

# Loggin button
loginButton = Button(frames,text='Log in',font=('Fc SaveSpace',20),fg='blue',bd=0,cursor='hand2',activebackground='white' , activeforeground='blue'
                ,command=login_page)
loginButton.place(x=200,y=569)

signup_window.mainloop()
