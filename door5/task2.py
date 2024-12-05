def function(i):
    global fake
    valid = True
    error = True
    handled = []
    for a in range(len(i)):
        for item in handled:
            if any(item in s for s in group[i[a]]) and valid:
                asd = item
                valid = False
                error = False
                fake = True
        if error:
            handled.append(i[a])
            error = True
        else:
            handled.insert(handled.index(asd), i[a])
    if not valid:
        handled = function(handled)
    if not fake:
        return["0"]
    return handled
        


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

for o in list:
    fake = False
    i = o.split(",")
    answer += int(function(i)[len(function(i))//2])

print(answer)

