import pymysql
import random
import time

x = random.randint(100,1000)
billnumber = ['Espresso','Cappucino','Latte','Mocha','Americano','Macchiato','Green Tea','Black Tea','Chocolate','White Chocolate','Milk','Thai Tea','Cupcake','Dounut','Cheesecake','Pudding','Waffle,','Cake']

sub = [55,40,45,50,20,50,30,40,30,40,30,35,55,30,75,80,65,70]

date = '100'


con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
mycursor = con.cursor()

query = 'use userdata'
mycursor.execute(query)

for i in range(0,18):
    # print(billnumber[i])
    # print(sub[i])
    query = 'insert into stock_main(coffee_name ,quantity , price) values(%s,%s,%s)'
    mycursor.execute(query,(billnumber[i],date,sub[i]))
con.commit()
con.close() 