from enterprise import * 
comp1 = Enterprise("comp1", 2300, 1978, "oleg1")
comp2 = Enterprise("comp2", 1000, 1232, "oleg2")
comp3 = Enterprise("comp3", 100, 2000, "oleg3")
comp4 = Enterprise("comp4", 11231, 2022, "oleg1")
comp5 = Enterprise("comp5", 99, 2012, "oleg2")
companies = [comp1, comp2, comp3, comp4, comp5]
for i in companies:
    if i.finance > 1000:
        i.DisplayAll()
        print("\n")
print("Компанії з однаковими власниками: \n")
for x in companies:
    checkName = x.owner
    counter = 0
    for i in companies:
        if checkName==i.owner:
            counter += 1
    if counter<2:
        companies.remove(x)
for i in companies:
    i.DisplayAll()