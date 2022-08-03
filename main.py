import argparse

mylist = ["d", "f"]

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='invest', help='add a new invest')
parser.add_argument('--remove', action='store', dest='remove', help='remove a invest from list')

args = parser.parse_args()
invest = (args.invest)
remove = (args.remove)
if (invest != None):
    print('Input add : ' + invest )
    mylist.append(invest)
    print(len(mylist))
    exit(0)
elif(remove != None):
    print('Input remove : ' + remove )
    exit(0)
print('Hello World!')
