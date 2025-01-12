import pymysql
import time
import COMMMAND

loop_item = 'Y'
loop_out = 'Y'


date = time.strftime('%d/%m/%Y')

con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
mycursor = con.cursor()

query = 'use userdata'
mycursor.execute(query)


sub_item = 0
select_choit = 0

while loop_out == 'Y':

    select_choit = int(input('What Do You Want To Do : '))

    if select_choit == 1:

        COMMMAND.Run_display()

        while loop_item == 'Y':
            try:
                
                get_item_name = input("Input you cargo : ")
                query = 'select price from stock_main where coffee_name = %s;'
                mycursor.execute(query,(get_item_name))
                row = mycursor.fetchone()
                x = list(row)[0]

                try:
                    get_item_many = int(input("how many you buy : "))
                    sub_item_in = x*get_item_many
                    sub_item += sub_item_in
                    print('Current Spending Amouny : ',sub_item)
                    loop_item = input("Want to buy another cargo Key Y : ")

                except:
                    print("Erroe, Please Follow Instruction.")

            except:
                print('Invalid Input Please Check Cargo Name.')

    elif select_choit == 2:
        get_many_employ = input("How Many Employee You Have ?: ")

        get_many_employ = get_item_many*12000

    elif select_choit == 3:

        query = 'insert into expenses(all_employee_salary ,stock_salary , Date_for_pay) values(%s,%s,%s)'
        mycursor.execute(query,(get_many_employ,sub_item,date))

        print('Save Sucessfuly')
        
    loop_out = input("Want to do another think Key Y : ") 
    
con.commit()
con.close() 