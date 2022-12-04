import konus as k
rad_max = int(input("Введіть більший радіус зрізаного конуса "))
rad_min = int(input("Введіть менший радіус зрізаного конуса "))
tvirna = int(input("Введіть довжину твірної зрізаного конуса "))
visota = int(input("Введіть висоту зрізаного конуса "))
print("Площа повної поверхні = ", k.square(rad_max, rad_min, tvirna))
print("Об'єм конуса = ", k.volume(rad_max, rad_min, visota))