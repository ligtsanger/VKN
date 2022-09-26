first = input("Введіть перший рядок ")
second = input("Введіть другий рядок ")
i = 0
b = 0
same = []
if len(first)>len(second):
    a = len(first)
    while i<a:
        for b in range(len(second)):
            if second[b]==first[i]:
                same.append(second[b])
        i += 1
else:
    a = len(second)
    while i<a:
        for b in range(len(first)):
            if first[b]==second[i]:
                same.append(first[b])
        i += 1
print(same) 