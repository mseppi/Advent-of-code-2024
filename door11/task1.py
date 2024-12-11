with open("input.txt", "r") as a:
    f = a.read().split()
a.close()


for a in range(75):
    temp = []
    for i in f:
        if i == "0":
            temp.append("1")
        elif len(i) % 2 == 0:
            l = i[:len(i)//2]
            r = i[len(i)//2:]
            temp.append(str(int(l)))
            temp.append(str(int(r)))
        else:
            temp.append(str(int(i)*2024))
    f = temp
    print(a)
print(len(f))