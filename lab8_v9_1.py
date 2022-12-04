from array import *
import random
mas_min = int(input("Введіть нижню межу випадкових чисел "))
mas_max = int(input("Введіть верхню межу випадкових чисел "))
arr = array('i',[])
for i in range(12):
    arr.append(random.randint(mas_min, mas_max))
print(arr)
print(sorted(arr))