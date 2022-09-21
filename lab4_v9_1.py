import math
x = int(input("Введть значення x"))
fx = (math.sin(x)-math.log10(x))/math.sqrt(7*x)+(math.pow((x+4), (2*x-8)))
print("f(x) = ", fx)