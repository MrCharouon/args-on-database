import os
path = (os.path.expanduser('~/.tsewl/'))
try:
    os.chdir(path)
    # print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    # print("Directory: {0} does not exist".format(path))
    os.mkdir(path)
