from tkinter import *
from tkinter import filedialog , messagebox
import random
import time
import pymysql


# Functions Logout
def logout_page():
    root.destroy()
    import Signin

# Functions Save
def reset():
    

    textReceipt.delete(1.0,END)
    e_esp1.set('0')
    e_esp2.set('0')

    e_cap1.set('0')
    e_cap2.set('0')

    e_lat1.set('0')
    e_lat2.set('0')

    e_moc1.set('0')
    e_moc2.set('0')

    e_ame1.set('0')
    e_ame2.set('0')

    e_mac1.set('0')
    e_mac2.set('0')

    e_green1.set('0')
    e_green2.set('0')

    e_black1.set('0')
    e_black2.set('0')

    e_choco1.set('0')
    e_choco2.set('0')

    e_white1.set('0')
    e_white2.set('0')

    e_milk1.set('0')
    e_milk2.set('0')

    e_thai1.set('0')
    e_thai2.set('0')

    e_cup.set('0')
    e_donut.set('0')
    e_chee.set('0')
    e_pud.set('0')
    e_waf.set('0')
    e_cake.set('0')

    textespresso.config(state=DISABLED)
    textespresso2.config(state=DISABLED)
    textcappucino.config(state=DISABLED)
    textcappucino2.config(state=DISABLED)
    textlatte.config(state=DISABLED)
    textlatte2.config(state=DISABLED)
    textmocha.config(state=DISABLED)
    textmocha2.config(state=DISABLED)
    textamericano.config(state=DISABLED)
    textamericano2.config(state=DISABLED)
    textmacchiato.config(state=DISABLED)
    textmacchiato2.config(state=DISABLED)
    
    textgreen.config(state=DISABLED)
    textgreen2.config(state=DISABLED)
    textblack.config(state=DISABLED)
    textblack2.config(state=DISABLED)
    textchoco.config(state=DISABLED)
    textchoco2.config(state=DISABLED)
    textwhite.config(state=DISABLED)
    textwhite2.config(state=DISABLED)
    textmilk.config(state=DISABLED)
    textmilk2.config(state=DISABLED)
    textthai.config(state=DISABLED)
    textthai2.config(state=DISABLED)

    textcupcake.config(state=DISABLED)
    textdonut.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    textpudding.config(state=DISABLED)
    textwaffle.config(state=DISABLED)
    textcake.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    costofcoffeevar.set('')
    costofteavar.set('')
    costofdessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

# Functions Save
def save():
    if textReceipt.get(1.0,END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data = textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your bill is succesfully Saved')

# Functions Cost
def Total_Cost():
    global priceofcoffee,priceoftea,priceofdessert,subtotalItem,quantityofcoffee,quantityoftea,quantityofdessert,subquantityItem
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0  or var5.get() != 0 or var6.get()  != 0 or var7.get()  != 0 \
        or var8.get() != 0 or var9.get()  != 0 or var10.get() != 0  or var11.get() != 0  or var12.get() != 0  or var13.get() != 0  \
        or var14.get()  != 0 or var15.get() != 0 or var16.get() != 0  or var17.get() != 0  or var18.get() != 0 :
        # Coffee Menu
        item1 = int(e_esp1.get())
        item2 = int(e_esp2.get())
        item3 = int(e_cap1.get())
        item4 = int(e_cap2.get())
        item5 = int(e_lat1.get())
        item6 = int(e_lat2.get())
        item7 = int(e_moc1.get())
        item8 = int(e_moc2.get())
        item9 = int(e_ame1.get())
        item10 = int(e_ame2.get())
        item11 = int(e_mac1.get())
        item12 = int(e_mac2.get())

        # Tea Menu
        item13 = int(e_green1.get())
        item14 = int(e_green2.get())
        item15 = int(e_black1.get())
        item16 = int(e_black2.get())
        item17 = int(e_choco1.get())
        item18 = int(e_choco2.get())
        item19 = int(e_white1.get())
        item20 = int(e_white2.get())
        item21 = int(e_milk1.get())
        item22 = int(e_milk2.get())
        item23 = int(e_thai1.get())
        item24 = int(e_thai2.get())

        # Dessert Menu
        item25 = int(e_cup.get())
        item26 = int(e_donut.get())
        item27 = int(e_chee.get())
        item28 = int(e_pud.get())
        item29 = int(e_waf.get())
        item30 = int(e_cake.get())

########################################################################
        con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
        mycursor = con.cursor()

        #sub total

        priceofcoffee = (item1*35) + (item2*55) + (item3*45) + (item4*60) + (item5*50) + (item6*65) + (item7*50) + (item8*65) \
                        + (item9*35) + (item10*55) + (item11*60) + (item12*70)

        priceoftea =  (item13*40) + (item14*45) + (item15*50) + (item16*60) + (item17*40) + (item18*45) + (item19*50) + (item20*60) \
                        + (item21*40) + (item22*45) + (item23*45) + (item24*55)

        priceofdessert = (item25*65) + (item26*40) + (item27*85) + (item28*90) + (item29*75) + (item30*80)

        quantityofcoffee = (item1*1) + (item2*1) + (item3*1) + (item4*1) + (item5*1) + (item6*1) + (item7*1) + (item8*1) \
                        + (item9*1) + (item10*1) + (item11*1) + (item12*1)

        quantityoftea =  (item13*1) + (item14*1) + (item15*1) + (item16*1) + (item17*1) + (item18*1) + (item19*1) + (item20*1) \
                        + (item21*1) + (item22*1) + (item23*1) + (item24*1)

        quantityofdessert = (item25*1) + (item26*1) + (item27*1) + (item28*1) + (item29*1) + (item30*1)

        #update database
        query = 'use userdata'
        mycursor.execute(query)

        es_item = item1 + item2
        ca_item = item3 + item4
        la_item = item5 + item6
        mo_item = item7 + item8
        am_item = item9 + item10
        ma_item = item11 + item12

        green_item = item13+ item14
        black_item = item15 + item16
        choco_item = item17 + item18
        white_item = item19 + item20
        milk_item = item21 + item22
        thai_item = item23 + item24
        
         
    
        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Espresso";'
        mycursor.execute(query,(es_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Cappucino";'
        mycursor.execute(query,(ca_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Latte";'
        mycursor.execute(query,(la_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Mocha";'
        mycursor.execute(query,(mo_item))
        
        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Americano";'
        mycursor.execute(query,(am_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Macchiato";'
        mycursor.execute(query,(ma_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Green Tea";'
        mycursor.execute(query,(green_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Black Tea";'
        mycursor.execute(query,(black_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "White Chocolate";'
        mycursor.execute(query,(choco_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "White Chocolate";'
        mycursor.execute(query,(white_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Milk";'
        mycursor.execute(query,(milk_item))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Thai Tea";'
        mycursor.execute(query,(thai_item))
        
        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Cupcake";'
        mycursor.execute(query,(item25))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Dounut";'
        mycursor.execute(query,(item26))
        
        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Cheesecake";'
        mycursor.execute(query,(item27))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Pudding";'
        mycursor.execute(query,(item28))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Cake";'
        mycursor.execute(query,(item29))

        query = 'update stock_main set quantity =quantity - %s where coffee_name = "Waffle";'
        mycursor.execute(query,(item30))
        



        subquantityItem = quantityofcoffee + quantityoftea + quantityofdessert

        costofcoffeevar.set(str(priceofcoffee)+' Bath')
        costofteavar.set(str(priceoftea)+' Bath')
        costofdessertvar.set(str(priceofdessert)+' Bath')

        subtotalItem = priceofcoffee + priceoftea + priceofdessert
        subtotalvar.set(str(subtotalItem) +' Bath')

        servicetaxvar.set('5 Bath')

        totalcost = subtotalItem + 5
        totalcostvar.set(str(totalcost)+' Bath')
       

        con.commit()
        con.close()
    else:
        messagebox.showerror('Error','No Item is selected')

# Functions Coffee

def Espresso():
    if var1.get()==1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0,END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_esp1.set('0')
    
    if var1.get()==1:
        textespresso2.config(state=NORMAL)
        textespresso2.delete(0,END)
        textespresso2.focus()
    else:
        textespresso2.config(state=DISABLED)
        e_esp2.set('0')

def Cappucino():
    if var2.get()==1:
        textcappucino.config(state=NORMAL)
        textcappucino.delete(0,END)
        textcappucino.focus()
    else:
        textcappucino.config(state=DISABLED)
        e_cap1.set('0')
    
    if var2.get()==1:
        textcappucino2.config(state=NORMAL)
        textcappucino2.delete(0,END)
        textcappucino2.focus()
    else:
        textcappucino2.config(state=DISABLED)
        e_cap2.set('0')

def Latte():
    if var3.get()==1:
        textlatte.config(state=NORMAL)
        textlatte.delete(0,END)
        textlatte.focus()
    else:
        textlatte.config(state=DISABLED)
        e_lat1.set('0')
    
    if var3.get()==1:
        textlatte2.config(state=NORMAL)
        textlatte2.delete(0,END)
        textlatte2.focus()
    else:
        textlatte2.config(state=DISABLED)
        e_lat2.set('0')

def Mocha():
    if var4.get()==1:
        textmocha.config(state=NORMAL)
        textmocha.delete(0,END)
        textmocha.focus()
    else:
        textmocha.config(state=DISABLED)
        e_moc1.set('0')
    
    if var4.get()==1:
        textmocha2.config(state=NORMAL)
        textmocha2.delete(0,END)
        textmocha2.focus()
    else:
        textmocha2.config(state=DISABLED)
        e_moc2.set('0')

def Americano():
    if var5.get()==1:
        textamericano.config(state=NORMAL)
        textamericano.delete(0,END)
        textamericano.focus()
    else:
        textamericano.config(state=DISABLED)
        e_ame1.set('0')
    
    if var5.get()==1:
        textamericano2.config(state=NORMAL)
        textamericano2.delete(0,END)
        textamericano2.focus()
    else:
        textamericano2.config(state=DISABLED)
        e_ame2.set('0')

def Macchiato():
    if var6.get()==1:
        textmacchiato.config(state=NORMAL)
        textmacchiato.delete(0,END)
        textmacchiato.focus()
    else:
        textmacchiato.config(state=DISABLED)
        e_mac1.set('0')
    
    if var6.get()==1:
        textmacchiato2.config(state=NORMAL)
        textmacchiato2.delete(0,END)
        textmacchiato2.focus()
    else:
        textmacchiato2.config(state=DISABLED)
        e_mac2.set('0')

# Functions Tea
def GreenTea():
    if var7.get()==1:
        textgreen.config(state=NORMAL)
        textgreen.delete(0,END)
        textgreen.focus()
    else:
        textgreen.config(state=DISABLED)
        e_green1.set('0')
    
    if var7.get()==1:
        textgreen2.config(state=NORMAL)
        textgreen2.delete(0,END)
        textgreen2.focus()
    else:
        textgreen2.config(state=DISABLED)
        e_green2.set('0')

def BlackTea():
    if var8.get()==1:
        textblack.config(state=NORMAL)
        textblack.delete(0,END)
        textblack.focus()
    else:
        textblack.config(state=DISABLED)
        e_black1.set('0')
    
    if var8.get()==1:
        textblack2.config(state=NORMAL)
        textblack2.delete(0,END)
        textblack2.focus()
    else:
        textblack2.config(state=DISABLED)
        e_black2.set('0')

def Chocolate():
    if var9.get()==1:
        textchoco.config(state=NORMAL)
        textchoco.delete(0,END)
        textchoco.focus()
    else:
        textchoco.config(state=DISABLED)
        e_choco1.set('0')
    
    if var9.get()==1:
        textchoco2.config(state=NORMAL)
        textchoco2.delete(0,END)
        textchoco2.focus()
    else:
        textchoco2.config(state=DISABLED)
        e_choco2.set('0')

def WhiteChocolate():
    if var10.get()==1:
        textwhite.config(state=NORMAL)
        textwhite.delete(0,END)
        textwhite.focus()
    else:
        textwhite.config(state=DISABLED)
        e_white1.set('0')
    
    if var10.get()==1:
        textwhite2.config(state=NORMAL)
        textwhite2.delete(0,END)
        textwhite2.focus()
    else:
        textwhite2.config(state=DISABLED)
        e_white2.set('0')

def Milk():
    if var11.get()==1:
        textmilk.config(state=NORMAL)
        textmilk.delete(0,END)
        textmilk.focus()
    else:
        textmilk.config(state=DISABLED)
        e_milk1.set('0')
    
    if var11.get()==1:
        textmilk2.config(state=NORMAL)
        textmilk2.delete(0,END)
        textmilk2.focus()
    else:
        textmilk2.config(state=DISABLED)
        e_milk2.set('0')

def ThaiTea():
    if var12.get()==1:
        textthai.config(state=NORMAL)
        textthai.delete(0,END)
        textthai.focus()
    else:
        textthai.config(state=DISABLED)
        e_thai1.set('0')
    
    if var12.get()==1:
        textthai2.config(state=NORMAL)
        textthai2.delete(0,END)
        textthai2.focus()
    else:
        textthai2.config(state=DISABLED)
        e_thai2.set('0')

# Functions Dessert
def Cupcake():
    if var13.get()==1:
        textcupcake.config(state=NORMAL)
        textcupcake.delete(0,END)
        textcupcake.focus()
    else:
        textcupcake.config(state=DISABLED)
        e_cup.set('0')

def Donut():
    if var14.get()==1:
        textdonut.config(state=NORMAL)
        textdonut.delete(0,END)
        textdonut.focus()
    else:
        textdonut.config(state=DISABLED)
        e_donut.set('0')

def Cheesecake():
    if var15.get()==1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.delete(0,END)
        textcheesecake.focus()
    else:
        textcheesecake.config(state=DISABLED)
        e_chee.set('0')

def Pudding():
    if var16.get()==1:
        textpudding.config(state=NORMAL)
        textpudding.delete(0,END)
        textpudding.focus()
    else:
        textpudding.config(state=DISABLED)
        e_pud.set('0')

def Waffle():
    if var17.get()==1:
        textwaffle.config(state=NORMAL)
        textwaffle.delete(0,END)
        textwaffle.focus()
    else:
        textwaffle.config(state=DISABLED)
        e_waf.set('0')

def Cake():
    if var18.get()==1:
        textcake.config(state=NORMAL)
        textcake.delete(0,END)
        textcake.focus()
    else:
        textcake.config(state=DISABLED)
        e_cake.set('0')

root = Tk()

root.geometry('1280x780+0+0')

root.resizable(0,0)

root.title('Menu Coffee System')
root.config(bg='black') # สี bg

topFrame = Frame(root,bd=10,relief=RIDGE,bg='dark orange',pady=10)
topFrame.pack(side=TOP)

LabelTitle = Label(topFrame,text='Coffee Menu',font=('Bebas',50,'bold'),fg='black',width=43)
LabelTitle.grid(row=0,column=0)

# frames
menuFrame = Frame(root,bd=10,relief=RIDGE,bg='dark orange')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame,bd=4,relief=RIDGE,bg='dark orange')
costFrame.pack(side=BOTTOM)

coffeeFrame = LabelFrame(menuFrame,text='Coffee\t         HOT  COLD',font=('Bebas Neue',20,'bold'),bd=5,relief=RIDGE,bg='gold',fg='black')
coffeeFrame.pack(side=LEFT)

teaFrame = LabelFrame(menuFrame,text='Tea\t\t HOT  COLD',font=('Bebas Neue',20,'bold'),bd=5,relief=RIDGE,bg='black',fg='Red')
teaFrame.pack(side=LEFT)

dessertFrame = LabelFrame(menuFrame,text='Dessert',font=('Bebas Neue',20,'bold'),bd=5,relief=RIDGE,bg='sandy brown',fg='black',padx=24)
dessertFrame.pack(side=LEFT)

rightFrame = Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack()

recieptFrame = Frame(rightFrame,bd=4,relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()


# Varriable Coffee
e_esp1 = StringVar()
e_esp2 = StringVar()

e_cap1 = StringVar()
e_cap2 = StringVar()

e_lat1 = StringVar()
e_lat2 = StringVar()

e_moc1 = StringVar()
e_moc2 = StringVar()

e_ame1 = StringVar()
e_ame2 = StringVar()

e_mac1 = StringVar()
e_mac2 = StringVar()

# Varriable Tea
e_green1 = StringVar()
e_green2 = StringVar()

e_black1 = StringVar()
e_black2 = StringVar()

e_choco1 = StringVar()
e_choco2 = StringVar()

e_white1 = StringVar()
e_white2 = StringVar()

e_milk1 = StringVar()
e_milk2 = StringVar()

e_thai1 = StringVar()
e_thai2 = StringVar()

# Varriable Dessert
e_cup = StringVar()
e_donut = StringVar()
e_chee = StringVar()
e_pud = StringVar()
e_waf = StringVar()
e_cake = StringVar()

# Set 0 Coffee
e_esp1.set('0')
e_esp2.set('0')

e_cap1.set('0')
e_cap2.set('0')

e_lat1.set('0')
e_lat2.set('0')

e_moc1.set('0')
e_moc2.set('0')

e_ame1.set('0')
e_ame2.set('0')

e_mac1.set('0')
e_mac2.set('0')

# Set 0 Tea
e_green1.set('0')
e_green2.set('0')

e_black1.set('0')
e_black2.set('0')

e_choco1.set('0')
e_choco2.set('0')

e_white1.set('0')
e_white2.set('0')

e_milk1.set('0')
e_milk2.set('0')

e_thai1.set('0')
e_thai2.set('0')

# Set 0 Dessert

e_cup.set('0')
e_donut.set('0')
e_chee.set('0')
e_pud.set('0')
e_waf.set('0')
e_cake.set('0')

# Varriable Cost
costofcoffeevar = StringVar()
costofteavar = StringVar()
costofdessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

# -----------------------------------------------------------------------------------------
# Coffee
espresso = Checkbutton(coffeeFrame,text='Espresso',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var1,bg='gold',fg='black'
            ,command=Espresso)
espresso.grid(row=0,column=0)

cappucino = Checkbutton(coffeeFrame,text='Cappucino',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var2,bg='gold',fg='black'
            ,command=Cappucino)
cappucino.grid(row=1,column=0)

latte = Checkbutton(coffeeFrame,text='Latte',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var3,bg='gold',fg='black'
            ,command=Latte)
latte.grid(row=2,column=0)

mocha = Checkbutton(coffeeFrame,text='Mocha',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var4,bg='gold',fg='black'
            ,command=Mocha)
mocha.grid(row=3,column=0)

americano = Checkbutton(coffeeFrame,text='Americano',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var5,bg='gold',fg='black'
            ,command=Americano)
americano.grid(row=4,column=0)

macchiato = Checkbutton(coffeeFrame,text='Macchiato',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var6,bg='gold',fg='black'
            ,command=Macchiato)
macchiato.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Espresso
textespresso = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_esp1)
textespresso.grid(row=0,column=1)
textespresso2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_esp2)
textespresso2.grid(row=0,column=2)

# Cappucino
textcappucino = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cap1)
textcappucino.grid(row=1,column=1)
textcappucino2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cap2)
textcappucino2.grid(row=1,column=2)

# Latte
textlatte = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_lat1)
textlatte.grid(row=2,column=1)
textlatte2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_lat2)
textlatte2.grid(row=2,column=2)

# Mocha
textmocha = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_moc1)
textmocha.grid(row=3,column=1)
textmocha2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_moc2)
textmocha2.grid(row=3,column=2)

# Americano
textamericano = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_ame1)
textamericano.grid(row=4,column=1)
textamericano2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_ame2)
textamericano2.grid(row=4,column=2)

# Macchiato
textmacchiato = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_mac1)
textmacchiato.grid(row=5,column=1)
textmacchiato2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_mac2)
textmacchiato2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
# Tea
greentea = Checkbutton(teaFrame,text='Green tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var7,bg='black',fg='Red',
            command=GreenTea)
greentea.grid(row=0,column=0)

blacktea = Checkbutton(teaFrame,text='Black tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var8,bg='black',fg='Red',
            command=BlackTea)
blacktea.grid(row=1,column=0)

chocolate = Checkbutton(teaFrame,text='Chocolate',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var9,bg='black',fg='Red',
            command=Chocolate)
chocolate.grid(row=2,column=0)

whitechocolate = Checkbutton(teaFrame,text='White Chocolate',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var10,bg='black',fg='Red',
            command=WhiteChocolate)
whitechocolate.grid(row=3,column=0)

milk = Checkbutton(teaFrame,text='Milk',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var11,bg='black',fg='Red',
            command=Milk)
milk.grid(row=4,column=0)

thaitea = Checkbutton(teaFrame,text='Thai Tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var12,bg='black',fg='Red',
            command=ThaiTea)
thaitea.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Green Tea
textgreen = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_green1)
textgreen.grid(row=0,column=1)
textgreen2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_green2)
textgreen2.grid(row=0,column=2)

# Black Tea
textblack = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_black1)
textblack.grid(row=1,column=1)
textblack2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_black2)
textblack2.grid(row=1,column=2)

# Chocolate
textchoco = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_choco1)
textchoco.grid(row=2,column=1)
textchoco2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_choco2)
textchoco2.grid(row=2,column=2)

# White Chocolate
textwhite = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_white1)
textwhite.grid(row=3,column=1)
textwhite2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_white2)
textwhite2.grid(row=3,column=2)

# Milk
textmilk = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_milk1)
textmilk.grid(row=4,column=1)
textmilk2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_milk2)
textmilk2.grid(row=4,column=2)

# Thai Tea
textthai = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_thai1)
textthai.grid(row=5,column=1)
textthai2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_thai2)
textthai2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
# Dessert
cupcake = Checkbutton(dessertFrame,text='Cupcake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var13,bg='sandy brown',fg='black',
            command=Cupcake)
cupcake.grid(row=0,column=0)

dounut = Checkbutton(dessertFrame,text='Dounut',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var14,bg='sandy brown',fg='black',
            command=Donut)
dounut.grid(row=1,column=0)

cheesecake = Checkbutton(dessertFrame,text='Cheesecake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var15,bg='sandy brown',fg='black',
            command=Cheesecake)
cheesecake.grid(row=2,column=0)

pudding = Checkbutton(dessertFrame,text='Pudding',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var16,bg='sandy brown',fg='black',
            command=Pudding)
pudding.grid(row=3,column=0)

waffle = Checkbutton(dessertFrame,text='Waffle',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var17,bg='sandy brown',fg='black',
            command=Waffle)
waffle.grid(row=4,column=0)

cake = Checkbutton(dessertFrame,text='Cake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var18,bg='sandy brown',fg='black',
            command=Cake)
cake.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Cupcake
textcupcake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cup)
textcupcake.grid(row=0,column=1)

# Donut
textdonut = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_donut)
textdonut.grid(row=1,column=1)

# Cheese cake
textcheesecake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_chee)
textcheesecake.grid(row=2,column=1)

# Pudding
textpudding = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_pud)
textpudding.grid(row=3,column=1)

# Waffle
textwaffle = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_waf)
textwaffle.grid(row=4,column=1)

# Cake
textcake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cake)
textcake.grid(row=5,column=1)

# -----------------------------------------------------------------------------------------
# Costlabels total
labelCostofCoffee = Label(costFrame,text='Cost of coffee',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofCoffee.grid(row=0,column=0)
textCostofCoffee = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofcoffeevar)
textCostofCoffee.grid(row=0,column=1,padx=54)

labelCostofTea = Label(costFrame,text='Cost of Tea',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofTea.grid(row=1,column=0)
textCostofTea = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofteavar)
textCostofTea.grid(row=1,column=1,padx=54)

labelCostofDessert = Label(costFrame,text='Cost of Dessert',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofDessert.grid(row=2,column=0)
textCostofDessert = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofdessertvar)
textCostofDessert.grid(row=2,column=1,padx=54)

labelSubtotal = Label(costFrame,text='Sub Total',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelSubtotal.grid(row=0,column=2)
textSubtotal = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=54)

labelServiceTax = Label(costFrame,text='Service Tax',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelServiceTax.grid(row=1,column=2)
textServiceTax = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=54)

labelTotalcost = Label(costFrame,text='Total Cost',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelTotalcost.grid(row=2,column=2)
textTotalcost = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalcost.grid(row=2,column=3 ,padx=54)

#-------------------------------------------------------------------------------------------

# Text area receipt
textReceipt = Text(recieptFrame,font=('Bebas Neue',15),bd=3,width=42,height=10)
textReceipt.grid(row=0,column=0)

# Function Receipt
def receipt():



    if costofcoffeevar.get() != '' or costofteavar.get() != '' or costofdessertvar.get() != '':
        x = random.randint(100,1000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'*'*42)
        textReceipt.insert(END,'\nItems:\t\t\t Cost of Items(Bath)\n')
        textReceipt.insert(END,'*'*42)

        con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
        mycursor = con.cursor()

        query = 'use userdata'
        mycursor.execute(query)
        
        # Coffee
        if e_esp1.get()!='0':
            textReceipt.insert(END,f'\nEspresso (HOT)\t\t\t{int(e_esp1.get())*55}\n\n')
            
        
        if e_esp2.get()!='0':
            textReceipt.insert(END,f'\nEspresso (COLD)\t\t\t{int(e_esp2.get())*35}\n\n')
        
        if e_cap1.get()!='0':
            textReceipt.insert(END,f'\nCappucino (HOT)\t\t\t{int(e_cap1.get())*45}\n\n')

        if e_cap2.get()!='0':
            textReceipt.insert(END,f'\nCappucino (COLD)\t\t\t{int(e_cap2.get())*60}\n\n')
        
        if e_lat1.get()!='0':
            textReceipt.insert(END,f'\nLatte (HOT)\t\t\t{int(e_lat1.get())*50}\n\n')
        
        if e_lat2.get()!='0':
            textReceipt.insert(END,f'\nLatte (COLD)\t\t\t{int(e_lat2.get())*65}\n\n')

        if e_moc1.get()!='0':
            textReceipt.insert(END,f'\nMocha (HOT)\t\t\t{int(e_moc1.get())*50}\n\n')

        if e_moc2.get()!='0':
            textReceipt.insert(END,f'\nMocha (COLD)\t\t\t{int(e_moc2.get())*65}\n\n')

        if e_ame1.get()!='0':
            textReceipt.insert(END,f'\nAmericano (HOT)\t\t\t{int(e_ame1.get())*35}\n\n')

        if e_ame2.get()!='0':
            textReceipt.insert(END,f'\nAmericano (COLD)\t\t\t{int(e_ame2.get())*55}\n\n')
        
        if e_mac1.get()!='0':
            textReceipt.insert(END,f'\nMacchiato (HOT)\t\t\t{int(e_mac1.get())*60}\n\n')

        if e_mac2.get()!='0':
            textReceipt.insert(END,f'\nMacchiato (COLD)\t\t\t{int(e_mac2.get())*70}\n\n')
        
        # Tea
        if e_green1.get()!='0':
            textReceipt.insert(END,f'\nGreen Tea (HOT)\t\t\t{int(e_green1.get())*40}\n\n')
        
        if e_green2.get()!='0':
            textReceipt.insert(END,f'\nGreen Tea (COLD)\t\t\t{int(e_green2.get())*45}\n\n')
        
        if e_black1.get()!='0':
            textReceipt.insert(END,f'\nBlack Tea (HOT)\t\t\t{int(e_black1.get())*50}\n\n')
        
        if e_black2.get()!='0':
            textReceipt.insert(END,f'\nBlack Tea (COLD)\t\t\t{int(e_black2.get())*60}\n\n')
        
        if e_choco1.get()!='0':
            textReceipt.insert(END,f'\nChocolate (HOT)\t\t\t{int(e_choco1.get())*40}\n\n')

        if e_choco2.get()!='0':
            textReceipt.insert(END,f'\nChocolate (COLD)\t\t\t{int(e_choco2.get())*45}\n\n')
        
        if e_white1.get()!='0':
            textReceipt.insert(END,f'\nWhite Chocolate (HOT)\t\t\t{int(e_white1.get())*50}\n\n')

        if e_white2.get()!='0':
            textReceipt.insert(END,f'\nWhite Chocolate (COLD)\t\t\t{int(e_white2.get())*60}\n\n')

        if e_milk1.get()!='0':
            textReceipt.insert(END,f'\nMilk (HOT)\t\t\t{int(e_milk1.get())*40}\n\n')

        if e_milk2.get()!='0':
            textReceipt.insert(END,f'\nMilk (COLD)\t\t\t{int(e_milk2.get())*45}\n\n')

        if e_thai1.get()!='0':
            textReceipt.insert(END,f'\nThai Tea (HOT)\t\t\t{int(e_thai1.get())*45}\n\n')

        if e_thai2.get()!='0':
            textReceipt.insert(END,f'\nThai Tea (COLD)\t\t\t{int(e_thai2.get())*55}\n\n')

        # Dessert
        if e_cup.get()!='0':
            textReceipt.insert(END,f'\nCupcake\t\t\t{int(e_cup.get())*65}\n\n')

        if e_donut.get()!='0':
            textReceipt.insert(END,f'\nDounut\t\t\t{int(e_donut.get())*40}\n\n')

        if e_chee.get()!='0':
            textReceipt.insert(END,f'\nCheesecake\t\t\t{int(e_chee.get())*85}\n\n')

        if e_pud.get()!='0':
            textReceipt.insert(END,f'\nPudding\t\t\t{int(e_pud.get())*90}\n\n')
        
        if e_waf.get()!='0':
            textReceipt.insert(END,f'\nWaffle\t\t\t{int(e_waf.get())*75}\n\n')

        if e_cake.get()!='0':
            textReceipt.insert(END,f'\nCake\t\t\t{int(e_cake.get())*80}\n\n')

        textReceipt.insert(END,'-'*67)
        if costofcoffeevar.get()!='0 Bath':
            textReceipt.insert(END,f'\nCost of Coffee\t\t\t{priceofcoffee} Bath\n\n')
        if costofteavar.get()!='0 Bath':
            textReceipt.insert(END,f'\nCost of Tea\t\t\t{priceoftea} Bath\n\n')
        if costofdessertvar.get()!='0 Bath':
            textReceipt.insert(END,f'\nCost of Dessert\t\t\t{priceofdessert} Bath\n\n')

        textReceipt.insert(END,f'Sub Total\t\t\t{subtotalItem} Bath\n\n')
        textReceipt.insert(END,f'Service Tax\t\t\t{5} Bath\n\n')
        textReceipt.insert(END,f'Total Cost\t\t\t{subtotalItem+5} Bath\n\n')
        textReceipt.insert(END,'-'*67)
        all_subtotal = subtotalItem + 5


        query = 'insert into bills_and_order_detalls(Bill_number,Date,Total) values(%s,%s,%s)'
        mycursor.execute(query,(billnumber,date,all_subtotal))

        con.commit()
        con.close()

    

    else:
        messagebox.showerror('Error','No Item is selected')


# -----------------------------------------------------------------------------------------
# Button

buttonTotal = Button(buttonFrame,text='Total',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5
            ,command=Total_Cost)
buttonTotal.grid(row=0,column=0)

buttonRecipt = Button(buttonFrame,text='Receipt',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5 
            ,command=receipt)
buttonRecipt.grid(row=0,column=1)

buttonSave = Button(buttonFrame,text='Save',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5
            ,command=save)
buttonSave.grid(row=0,column=2)

buttonReset = Button(buttonFrame,text='Reset',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5
            ,command=reset)
buttonReset.grid(row=0,column=4)

buttonLogout = Button(buttonFrame,text='Logout',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5
            ,command=logout_page)
buttonLogout.grid(row=0,column=5)

# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Calculator
operator = ''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0,END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator = ''


calculatorField = Entry(calculatorFrame,font=('Bebas Neue',15),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7 = Button(calculatorFrame,text='7',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8 = Button(calculatorFrame,text='8',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9 = Button(calculatorFrame,text='9',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus = Button(calculatorFrame,text='+',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4 = Button(calculatorFrame,text='4',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5 = Button(calculatorFrame,text='5',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6 = Button(calculatorFrame,text='6',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus = Button(calculatorFrame,text='-',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1 = Button(calculatorFrame,text='1',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2 = Button(calculatorFrame,text='2',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3 = Button(calculatorFrame,text='3',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult = Button(calculatorFrame,text='*',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns = Button(calculatorFrame,text='Ans',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear = Button(calculatorFrame,text='Clear',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=clear)
buttonClear.grid(row=4,column=1)

button0 = Button(calculatorFrame,text='0',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDive = Button(calculatorFrame,text='/',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('/'))
buttonDive.grid(row=4,column=3)

root.mainloop() 