import matplotlib.pyplot as plt
with open("D:\\git\\VKN\\text.txt", "r") as f:
    text = f.read()
text = text.split(" ")
wordlist = []
counterlist  = []
for x in text:
    checkword = x
    counter = 0
    for i in text:
        if i == checkword:
            counter += 1
    wordlist.append(checkword)
    counterlist.append(counter)
plt.bar(wordlist, counterlist)
plt.show()