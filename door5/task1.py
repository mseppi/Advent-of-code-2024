answer = 0

with open("input.txt", "r") as a:
    f = a.read()
f = f.split("\n")
list = []
list2 = []

for item in f:
    if item != "":
        list.append(item)
    else:
        list2 = list
        list = []

group = {}
for i in list2:
    o = i.split("|")
    if o[0] not in group:
        group[o[0]] = []
    if o[0] in group:
        group[o[0]].append(o[1])

for a in list:
    i = a.split(",")
    valid = True
    handled = []
    for a in range(len(i)):
        for item in handled:
            if any(item in s for s in group[i[a]]):
                valid = False
        handled.append(i[a])
    if valid:
        answer += int(handled[len(handled)//2])
print(answer)