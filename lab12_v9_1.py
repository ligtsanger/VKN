import math
def square_solution(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=round((-b+d**0.5)/(2*a), 2)
        x2=round((-b-d**0.5)/(2*a), 2)
        return (x1,x2)
    elif d == 0:
        return (-b/(2*a),)
    else:
        print("Дійсних коренів немає")
def be_square_solution(a,b,c):
    tmp=square_solution(a,b,c)
    r=[]
    for a in tmp:
        if a>= 0:
            r.append(round((a**0.5), 2))
            temp_a = round(a, 2)
            r.append(-(temp_a**0.5))
    return r    
print("Введіть коефіцієнти квадратного рівняння")
print("ax^2 + bx + c = 0:")
x = float(input("a = "))
y = float(input("b = "))
z = float(input("c = "))
print("Корені рівняння: ", square_solution(x, y, z))
print("Введіть коефіцієнти біквадратного рівняння")
print("ax^4 + bx^2 + c = 0:")
x = float(input("a = "))
y = float(input("b = "))
z = float(input("c = "))
print("Корені рівняння: ", be_square_solution(x, y, z))