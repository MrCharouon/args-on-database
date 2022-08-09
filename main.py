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
parser.add_argument('--add', action='store', dest='invest', help='add a new invest')
parser.add_argument('--remove', action='store', dest='remove', help='remove a invest from list')

args = parser.parse_args()
invest = (args.invest)
remove = (args.remove)
if (invest != None):
    INSERT_DATA(invest, list_id)
    result = update_db()
    r = result.update()
    print('The investment has been successfully added to the database : ' + invest + "\n" )
    print('your investments are : ' + str(r))
    exit(0)
elif(remove != None):
    DELETE_DATA(remove)
    result = update_db()
    r = result.update()
    print('The investment has been successfully added to the database : ' + remove + "\n" )
    print('your investments are : ' + str(r))
    exit(0)


result = update_db()
r = result.update()
if (len(r) == 0):
    print ("هنوز سهمی اضافه نکرده اید"+ "\n" +  "برای راهنمایی دستور زیر را اجرا کنید" + "\n" + "main.py -h")
else:
    print('your investments are : ' + str(r))
