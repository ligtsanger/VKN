import numpy as np
import random
import array
M = int(input("Введіть кількість рядків "))
N = int(input("Введіть кількість стовпців "))
arr1=np.zeros((M,N)) 
for i in range(M):     
    for j in range (N):         
        arr1[i][j]=random.randint(1,50) 
arr2=np.zeros((M,N)) 
for i in range(M):     
    for j in range (N):         
        arr2[i][j]=random.randint(1,50)
print("Сума = \n", arr1+arr2)
print("Різниця = \n",arr1-arr2)
print("Добуток = \n",arr1*arr2)