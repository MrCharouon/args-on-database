import argparse
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS invests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_invests Text );""")
conn.commit()

def Insert_Data(value):
    number = "2"
    query = f'INSERT INTO invests VALUES ("{number}", "{value}")'
    cur.execute(query)
    conn.commit()
    conn.close()


parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='invest', help='add a new invest')
parser.add_argument('--remove', action='store', dest='remove', help='remove a invest from list')

args = parser.parse_args()
invest = (args.invest)
remove = (args.remove)
if (invest != None):
    print('Input add : ' + invest )
    Insert_Data(invest)
    exit(0)
elif(remove != None):
    print('Input remove : ' + remove )
    exit(0)
print('Hello World!')
