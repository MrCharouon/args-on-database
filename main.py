import argparse
from directory import *
from db_connection import *

directorycheck()

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='a_invest', help='add a new invest to datebase')
parser.add_argument('--remove', action='store', dest='r_invest', help='remove a invest from your watchlist')

args = parser.parse_args()
invest = (args.a_invest)
remove = (args.r_invest)
if(invest != None):
    def check(w, list):
        if w in list:
            print("The investment is in the database!")
        else:
            INSERT_DATA(invest, list_id)
            print('The investment has been successfully added to the database : ' + invest + "\n" )

    check(invest,list_invests)
    result = update_db()
    r = result.update()
    print('your investments are : ' + str(r))
    exit(0)
elif(remove != None):
    def check(w, list):
        if w in list:
            DELETE_DATA(remove)
            result = update_db()
            r = result.update()
            print('The investment has been successfully remove on database : ' + remove + "\n" )
            print('your investments are : ' + str(r))
            
        else:
            print ("Investments of this kind do not exist!")

    check(remove,list_invests)
    exit(0)
result = update_db()
r = result.update()
if (len(r) == 0):
    print ("هنوز سهمی اضافه نکرده اید"+ "\n" +  "برای دیدن دستورات بیشتر اجرا کنید : main.py --help"  + "\n" )
else:
    print('your investments are : ' + str(r))
