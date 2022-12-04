import json

with open("D:\\git\\VKN\\posts.json") as file:
    data = json.load(file)
recordsCount = int(input("Введіть кількість записів для додавання "))
if recordsCount > 0:
    for i in range(len(data), len(data)+recordsCount):
        userid =  int(input("Введіть userid "))
        id = int(input("Введіть id "))
        title =  input("Введіть title ")
        body = input("Введіть body ")
        d = {}
        d["userId"]=userid
        d["id"]=id
        d["title"]=title
        d["body"]=body
        data.append(d)
    json_obj = json.dumps(data, indent=2)
    with open("D:\\git\\VKN\\posts.json", "w") as file:
        file.write(json_obj)
searchid = int(input("Введіть id для пошуку "))
for i in data:
    if i["userId"]==searchid:
        print(i)