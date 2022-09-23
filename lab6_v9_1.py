import math
a = float(input("Введіть нижню межу табулювання"))
b = float(input("Введіть верхню межу табулювання"))
c = float(input("Введіть крок табулювання"))
spisokx = []
spisokfx = []
spisok1 = [spisokx, spisokfx]
for i in range(100):
    fx = math.fabs(math.tan(math.fabs(a)+1))
    a = round(a, 2)
    fx = round(fx, 2)
    spisokx.append(a)
    spisokfx.append(fx)
    print("x = ", i, " ", "fx = ", fx, "Крок №", i)
    a += c
    if a>b:
        break
    i +=1
print(spisok1)
