import math
x = float(input("Введіть значення х "))
y = float(input("Введіть значення y "))
S = math.cos(x)*math.tan(y)+math.log((pow(math.e, x)+4), 5)+1/(math.sqrt(math.fabs(x)+0.1))
print("S = ", S)