import pymysql

try:
    con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
    mycursor = con.cursor()

except:
    print('Error','Database Connectivity Issue, Please check You Password Or User And Try Again')

try:
    query = 'use userdata'
    mycursor.execute(query)

except:
    print('Error',"Don't Have Database")

try:
    query = 'Create table stock_main(goods_id int auto_increment key not null ,coffee_name varchar(50) ,quantity int(100) ,price int(100))'
    mycursor.execute(query)

except:
    try:
        query = 'Create table bills_and_order_detalls(Sales_id int auto_increment key not null ,Bill_number varchar(50) ,Date varchar(100), Total varchar(50))'
        mycursor.execute(query)

    except:
        try:
            query = 'Create table expenses(expenses_id int auto_increment key not null ,all_employee_salary varchar(50) ,stock_salary varchar(50),Date_for_pay varchar(100))'
            mycursor.execute(query)
        
        except:
            print('Error','You Already Create This Table')
