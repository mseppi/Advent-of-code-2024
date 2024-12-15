with open("input.txt", "r") as a:
    f = a.readlines()
    f = [i.replace("\n", "") for i in f]
a.close()

handled = set()


def check(i, a):
    global perimeter
    global area
    global handled
    if (i, a) in handled:
        return
    handled.add((i, a))
    area += 1
    if i + 1 >= len(f) or f[i + 1][a] != f[i][a]:
        perimeter += 1
    else:
        check(i + 1, a)
    if i - 1 < 0 or f[i - 1][a] != f[i][a]:
        perimeter += 1
    else:
        check(i - 1, a)
    if a + 1 >= len(f[i]) or f[i][a + 1] != f[i][a]:
        perimeter += 1
    else:
        check(i, a + 1)
    if a - 1 < 0 or f[i][a - 1] != f[i][a]:
        perimeter += 1
    else:
        check(i, a - 1)
    
answer = 0
for i in range(len(f)):
    for a in range(len(f[i])):
        perimeter = 0
        area = 0
        check(i, a)
        answer += perimeter * area
print(answer)