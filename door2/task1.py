f = open("input.txt", "r")
answer = 0
for i in f:
    safe = True
    i = i.split(" ")
    i[-1] = i[-1].replace("\n", "")
    i = list(map(int, i))
    if i[0] > i[1]:
        for a in range(len(i) - 1):
            if i[a] - i[a + 1] > 3 or i[a] - i[a + 1] <= 0:
                safe = False
                break
    elif i[0] < i[1]:
        for a in range(len(i) - 1):
            if i[a + 1] - i[a] > 3 or i[a + 1] - i[a] <= 0:
                safe = False
                break
    else:
        safe = False
    if safe:
        answer += 1
print(answer)