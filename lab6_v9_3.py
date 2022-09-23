import math
a = float(input("Введіть нижню межу табулювання"))
b = float(input("Введіть верхню межу табулювання"))
c = float(input("Введіть крок табулювання"))
i = 0
while a<b:
    fx = math.fabs(math.tan(math.fabs(a)+1))
    print("x = ", round(a,2), " ", "fx = ", round(fx, 2), "Крок №", i)
    a += c
    i += 1