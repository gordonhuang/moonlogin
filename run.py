import os

f = open("user.txt", "r").read()
os.system("cmd /k ssh " + f)

