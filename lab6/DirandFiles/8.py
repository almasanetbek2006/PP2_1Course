import os

file = 'test2.py'

if not os.path.exists(file):
    print("No such file")

location = r'C:\Users\User\Desktop\PP2_WWW\lab6'

path = os.path.join(location, file)

os.remove(path)