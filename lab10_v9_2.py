import os
import shutil
print(os.listdir("D:\\git\\VKN\\lab10"))
anames = []
bnames = []
for i in os.listdir("D:\\git\\VKN\\lab10"):
    if i[0] == "a":
        anames.append(i)
    elif i[0] == "b":
        bnames.append(i)
os.mkdir("D:\\git\\VKN\\lab10\\A_NAMES")
os.mkdir("D:\\git\\VKN\\lab10\\B_NAMES")
for i in anames:
    pardir = "D:\\git\\VKN\\lab10\\"+i
    shutil.move(pardir, "D:\\git\\VKN\\lab10\\A_NAMES")
for i in bnames:
    pardir = "D:\\git\\VKN\\lab10\\"+i
    shutil.move(pardir, "D:\\git\\VKN\\lab10\\B_NAMES")
