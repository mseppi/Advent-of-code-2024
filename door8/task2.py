import copy

with open("input.txt", "r") as file:
    f = [i.replace("\n", "") for i in file.readlines()]
chara = set()
for i in f:
    for a in i:
        if a != ".":
            chara.add(a)
dict = {}
for u in chara:
    dict[u] = []
    for i in range(len(f)):
        for o in range(len(f[i])):
            if f[i][o] == u:
                dict[u].append((i, o))

places = set()

lines = (len(f), len(f[0]))

for i in dict:
    for a in range(len(dict[i])):
        temp = list(dict[i][a+1:])
        for o in temp:
            x1, x2 = o
            y1, y2 = dict[i][a]
            places.add((y1, y2))
            places.add((x1, x2))
            z1, z2 = x1-y1, x2-y2
            less1, less2 = y1-z1, y2-z2
            more1, more2 = x1+z1, x2+z2
            while 0<=less1<lines[0] and 0<=less2<lines[1]:
                places.add((less1, less2))
                less1, less2 = less1-z1, less2-z2
            while 0<=more1<lines[0] and 0<=more2<lines[1]:
                places.add((more1, more2))
                more1, more2 = more1+z1, more2+z2            

print(len(places))