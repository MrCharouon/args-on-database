import argparse
from directory import *
from db_connection import *

directorycheck()

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='a_invest', help='add a new invest to datebase')
parser.add_argument('--remove', action='store', dest='r_invest', help='remove a invest from your watchlist')

args = parser.parse_args()
stock_input_add = (args.a_invest)
stock_input_remove = (args.r_invest)
if(stock_input_add != None):
    def check(w, list):
        if w in list:
            print("\n"+ "این سهم رو قبلا اضافه کردی")
        else:
            INSERT_DATA(id_keys_list, stock_input_add)
            print("\n"+ 'سهم با موفقیت به پایگاه داده اضافه شد : ' + stock_input_add )

    check(stock_input_add,stock_keys_list)
    result = update_db()
    r = result.update()
    print("\n"+ 'your investments are : ' + str(r)+ "\n")
    exit(0)
elif(stock_input_remove != None):
    def check(w, list):
        if w in list:
            DELETE_DATA(stock_input_remove)
            print("\n"+ 'سهم با موفقیت از پایگاه داده حذف شد : ' + stock_input_remove)
            
        else:
            print ("\n"+ "چنین سهمی وجود ندارد")

    check(stock_input_remove,stock_keys_list)
    result = update_db()
    r = result.update()
    print("\n"+ 'your investments are : ' + str(r)+ "\n")
    exit(0)
result = update_db()
r = result.update()
if (len(r) == 0):
    print ("\n"+ "هنوز سهمی اضافه نکرده اید"+ "\n"+ "برای دیدن دستورات بیشتر اجرا کنید"+ "\n"+ "main.py --help"+ "\n")
else:
    print("\n"+ 'your investments are : ' + str(r)+ "\n")
