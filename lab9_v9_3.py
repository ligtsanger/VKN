import math
triangles = {'first': '10 20 25', 
'second': '20 30 40', 
'third': '10 30 35'}
def square(sidelist):
        a = sidelist[0]
        b = sidelist[1]
        c = sidelist[2]
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
max_square = 0
max_triangle = ""
for i in triangles:
       args = triangles[i].split(" ")
       args = [int(x) for x in args]
       if square(args)>max_square:
                max_square=square(args)
                max_triangle = i
print("Максимальна площа =", max_square, "трикутник:", max_triangle)