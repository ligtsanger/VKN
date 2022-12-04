import csv
import math
def func(x):
    res = math.pow(math.e, x)+0.1*math.pow(x, 2)
    return res
with open("D:\\git\\VKN\\func.csv", "w") as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow(["x", "y"])
with open("D:\\git\\VKN\\func.csv", "a") as f:
    writer = csv.writer(f, delimiter=" ")
    min = int(input("Введіть нижню межу табулювання функції "))
    max = int(input("Введіть верхню межу табулювання функції "))
    for i in range(min, max+1):
        output =  str(func(i))
        print(str(output))
        writer.writerow([i, output])
        