import math
x = float(input("Введіть значення х "))
if x>7:
    y = 2.27*math.pow(math.e, 4*x+1)+3
    print("1")
elif x<=7 and x>=0.5:
    y = math.pow(0.64*x, (x+0.1))
    print("2")
else:
    y = math.log(math.fabs(x-math.exp(x)), math.e)
    print("3")
print("y = ", y)