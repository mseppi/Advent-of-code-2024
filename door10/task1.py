with open("input.txt", "r") as a:
    f = a.readlines()
    f = [i.replace("\n", "") for i in f]
a.close()



answer = set()

def check(i, a, y, og_i, og_a):
    if y == 9:
        answer.add((og_i, og_a, i, a))
        return
    if i + 1 < len(f) and int(f[i + 1][a]) == y + 1:
        check(i + 1, a, y + 1, og_i, og_a)
    if i - 1 >= 0 and int(f[i - 1][a]) == y + 1:
        check(i - 1, a, y + 1, og_i, og_a)
    if a + 1 < len(f[i]) and int(f[i][a + 1]) == y + 1:
        check(i, a + 1, y + 1, og_i, og_a)
    if a - 1 >= 0 and int(f[i][a - 1]) == y + 1:
        check(i, a - 1, y + 1, og_i, og_a)
    return

for i in range(len(f)):
    for a in range(len(f[i])):
        if f[i][a] == "0":
            check(int(i), int(a), 0, int(i), int(a))

print(len(answer))

