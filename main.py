import argparse
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS invests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_invests Text );""")
conn.commit()

list_invests = []
list_id = []
sql_select_Query = "select * from invests"
cursor = conn.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    list_id.append(row[0])
    list_invests.append(row[1])

def INSERT_DATA(new_invest, db_ids):
    if len(list_id) == 0:
        number_id = 1
    else:
        number_id = int(list_id[-1])+1
    query = f'INSERT INTO invests VALUES ("{number_id}", "{new_invest}")'
    cur.execute(query)
    conn.commit()

def DELETE_DATA(delete_invest):
    query = f'DELETE FROM invests WHERE user_invests = "{delete_invest}"'
    cur.execute(query)
    conn.commit()

class update_db():
    def update(slef):
        update_invest = []
        sql_select_Query = "select * from invests"
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            update_invest.append(row[1])
        conn.close()
        return (update_invest)

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='a_invest', help='add a new invest to datebase')
parser.add_argument('--remove', action='store', dest='r_invest', help='remove a invest from your watchlist')



args = parser.parse_args()
invest = (args.a_invest)
remove = (args.r_invest)
if (invest != None):
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
