class River():
    def __init__(self, name, continent, length):
        self.name = str(name)
        self.continent = str(continent)
        self.length = int(length)
    def rename(self, new_name):
        self.name = str(new_name)
    def set_length(self, new_length):
        self.length = int(new_length)
Amazonka = River("Амазонка", "Південна Америка", 7100)
Nil = River("Ніл","Африка", 6670)
Nigger = River("Нігер", "Африка", 4350)
rivers = [Amazonka, Nil, Nigger]
print("Введення нової річки")
rname = input("Введіть назву ")
rcontinect = input("Введіть континент ")
rlength = int(input("Введіть довжину "))
new_river = River(rname, rcontinect, rlength)
rivers.append(new_river)
print("",new_river.name, "\n", new_river.continent, "\n", new_river.length)
nname = input("Введіть нове ім'я річки ")
nlength = input("Введіть нову довжину річки ")
print(Nil.name)
print(Nil.length)
Nil.rename(nname)
Nil.set_length(nlength)
print(Nil.name)
print(Nil.length)