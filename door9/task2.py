with open("input.txt", "r") as a:
    f = a.read()
a.close()

list = []
for i, c in enumerate(f):
    if i % 2:
        index = None
    else:
        index = i // 2
    size = int(c)
    if size > 0:
        list.append([index, size])


i = 0
while i < len(list):
    i += 1
    index, size = list[-i]
    if index is None:
        continue

    for u in range(len(list)-i):
        if list[u][0] is None and list[u][1] >= size:
            if list[u][1] == size:
                list[u][0] = index
            else:
                list[u][1] -= size
                list.insert(u, list[-i].copy())
            list[-i][0] = None
            break

total = index = 0
for id, size in list:
    if id is not None:
        total += id * size * (index + ((size - 1) / 2))
    index += size


print(int(total))