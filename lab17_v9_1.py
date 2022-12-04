import pandas as pd
df = pd.read_csv("D:git\\VKN\\input.csv", sep=",", encoding="cp1251")
for i in range(3):
    name = "Firm"+str(i+1)
    sum = 0
    for i in df[name]:
       sum = sum+i
    print(f"Сумма фірми {name}")
    print(sum)
    