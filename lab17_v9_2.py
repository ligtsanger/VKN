import pandas as pd
golos = "аеєуояиі"
with open("D:\\git\\VKN\\text_1.txt", "r") as f:
    text = f.read()
    for i in text:
        i = i.lower()
df = pd.Series(text)
golos_list = []
text = df[0]
text = text.split(" ")
for i in text:
    counter = 0 
    for x in i:
        if x.lower() in golos:
            counter +=1
    if counter>=3:
        golos_list.append(i)
with open("D:\\git\\VKN\\text_final.txt", "w") as f:
    for i in golos_list:
        f.write(i+"\n")