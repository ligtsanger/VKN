A = {i*2 for i in range(100)}
B = {i*3 for i in range(100)}
C = {i*5 for i in range(100)}
D = {i*10 for i in range(50)}
F = {i*15 for i in range(34)}
print(A)
print("Числа, що діляться на 30", A&B&C)
print("Числа, що діляться на 15 та не діляться на 2", B&C-D)
print("Числа, що діляться на 5 та не діляться на 2, 3", C-(D|F))