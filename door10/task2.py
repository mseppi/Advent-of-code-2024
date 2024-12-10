with open("input.txt", "r") as a:
    f = a.readlines()
    f = [i.replace("\n", "") for i in f]
a.close()

answer = 0

def check (i, a, y):
    global answer
    if y == 9:
        answer += 1
        return
    if i + 1 < len(f) and int(f[i + 1][a]) == y + 1:
        check(i + 1, a, y + 1)
    if i - 1 >= 0 and int(f[i - 1][a]) == y + 1:
        check(i - 1, a, y + 1)
    if a + 1 < len(f[i]) and int(f[i][a + 1]) == y + 1:
        check(i, a + 1, y + 1)
    if a - 1 >= 0 and int(f[i][a - 1]) == y + 1:
        check(i, a - 1, y + 1)
    return

for i in range(len(f)):
    for a in range(len(f[i])):
        if f[i][a] == "0":
            check(int(i), int(a), 0)

print(answer)