test = ["https://facebook.com", "google.com", "http://wikipedia.org", "https://twitter.com", "youtube.com", "microsoft.com"]
def wo_protocol(N, sites):
    no_protocol = []
    counter = 0
    for i in sites:
        if str(i).find("https://") == -1 and str(i).find("http://") == -1:
            no_protocol.append(i)
            counter +=1
        if counter == N:
            break
    print(no_protocol)
count = int(input("Введіть кількість сайтів для виведення "))
wo_protocol(count,test)

