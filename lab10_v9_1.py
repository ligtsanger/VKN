def get_key(dict, value):
    for k, v in dict.items():
        if v == value:
            return k
d = {}
f =  open("D:\\git\\VKN\\start.txt", 'r')
for line in f:
    key, *value = line.split()
    d[key] = value
f.close()
squares = []
countries = open("D:\\git\\VKN\\countries.txt", 'w')
sqrs = open("D:\\git\\VKN\\squares.txt", 'w')
for i in d:
    arg = d[i]
    arg = [int(x) for x in arg]
    arg = arg[0]
    countries.write(i + '\n')
    squares.append(arg)
    arg = str(arg)
    sqrs.write(arg + '\n')
countries.close()
sqrs.close()
val = []
val.append(str(max(squares)))
country = get_key(d, val)
largest = open("D:\\git\\VKN\\largest.txt", 'w')
largest.write(country + '\n')
largest.write(str(max(squares)) + '\n')