ryad = input("Введіть рядок слів, розілених пробілами ")
slova = ryad.split(" ")
max_length = slova[0]
for i in range(len(slova)):
    if slova[i-1]>max_length:
        max_length=slova[i]
print("Найдовше слово складається з ", len(max_length), "символів,", "це слово:", max_length)