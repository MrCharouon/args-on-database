import argparse
import sqlite3
# def Create_Database():
conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS invests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_invests Text );""")
conn.commit()
def INSERT_DATA(new_invest, db_ids):
    if len(list_id) == 0:
        number_id = 1
    else:
        number_id = int(list_id[-1])+1
    result = tttt()
    r = result.bbb()
    print(r)
    query = f'INSERT INTO invests VALUES ("{number_id}", "{new_invest}")'
    cur.execute(query)
    conn.commit()
    conn.close()
def DELETE_DATA(delete_invest):
    query = f'DELETE FROM invests WHERE user_invests = "{delete_invest}"'
    cur.execute(query)
    conn.commit()
    conn.close()

class tttt():

    def aaa(slef):
        a = "ali"
        return (a)  
    def bbb(slef):
        b = "mehdi"
        return (b)     

list_invests = []
list_id = []
sql_select_Query = "select * from invests"
cursor = conn.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    # print("id = ", row[0], )
    # print("user_invests = ", row[1])
    list_id.append(row[0])
    list_invests.append(row[1])
    # print("--------------------------------------------")
# print(list_invests)

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='invest', help='add a new invest')
parser.add_argument('--remove', action='store', dest='remove', help='remove a invest from list')

args = parser.parse_args()
invest = (args.invest)
remove = (args.remove)
if (invest != None):
    print('The investment has been successfully added to the database : ' + invest )
    print('your investments are : ' + str(list_invests))
    INSERT_DATA(invest, list_id)
    exit(0)
elif(remove != None):
    print('The investment has been successfully removed to the database : ' + remove )
    print('your investments are : ' + str(list_invests))
    DELETE_DATA(remove)
    exit(0)
print('Hello World!')
