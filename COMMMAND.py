import colorama
from colorama import Back , Fore , Style
import pymysql

colorama.init(autoreset=True)


def Run_display():

    import pymysql

    list_row = []

    con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
    mycursor = con.cursor()

    query = 'use userdata'
    mycursor.execute(query)

    query = 'select price from stock_main ;'
    mycursor.execute(query)
    row = mycursor.fetchall()
    for i in row:
        list_row.append(i[0])

    s1 = list_row[0] ; s2 = list_row[1] ; s3 = list_row[2] ; s4 = list_row[3] ; s5 = list_row[4] ; s6 = list_row[5] ; s7 = list_row[6]; s8 = list_row[7] ; s9 = list_row[8] ; s10 = list_row[9] ; s11 = list_row[10] ; s12 = list_row[11];  s13 = list_row[12];  s14 = list_row[13];  s15= list_row[14]; s16 = list_row[15] ; s17 = list_row[16] ; s18 = list_row[17]


    print(Back.GREEN+'='*160)
    print('')
    print(Fore.MAGENTA+'\t\t\t\t\t\t\t\t\t    STOCK')
    print(Fore.RED+'\t\tCoffee\t\t\t\tPRICE\t\tTEA\t\t\t\tPRICE\t\t\tDESSERT\t\t\tPRICE')
    print(Fore.YELLOW+'\t\tEspresso\t\t\t',s1,'\t\tGreen Tea\t\t\t',s7,'\t\t\tCupcake\t\t\t',s13,'')
    print(Fore.YELLOW+'\t\tCappucino\t\t\t',s2,'\t\tBlack Tea\t\t\t',s8,'\t\t\tDonut\t\t\t',s14,'')
    print(Fore.YELLOW+'\t\tLatte\t\t\t\t',s3,'\t\tChocolate\t\t\t',s9,'\t\t\tCheesecake\t\t',s15,'')
    print(Fore.YELLOW+'\t\tMocha\t\t\t\t',s4,'\t\tWhite Chocolate\t\t\t',s10,'\t\t\tPudding\t\t\t',s16,'')
    print(Fore.YELLOW+'\t\tAmericano\t\t\t',s5,'\t\tMilk\t\t\t\t',s11,'\t\t\tWaffle\t\t\t',s17,'')
    print(Fore.YELLOW+'\t\tMacchiato\t\t\t',s6,'\t\tThai Tea\t\t\t',s12,'\t\t\tCake\t\t\t',s18,'')

    print('')
    print(Back.GREEN+'='*160)

    con.commit()
    con.close() 



        
