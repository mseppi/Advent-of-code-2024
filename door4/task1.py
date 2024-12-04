answer = 0

with open("input.txt", "r") as a:
    f = a.read()
f = f.split("\n")
for i in range(len(f)):
    for a in range(len(f[i])):
        try:
            if f[i][a] == "X" and f[i][a + 1] == "M" and f[i][a + 2] == "A" and f[i][a + 3] == "S" and a + 3 < len(f[i]):
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i][a - 1] == "M" and f[i][a - 2] == "A" and f[i][a - 3] == "S" and a - 3 >= 0:
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i + 1][a] == "M" and f[i + 2][a] == "A" and f[i + 3][a] == "S" and i + 3 < len(f):
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i - 1][a] == "M" and f[i - 2][a] == "A" and f[i - 3][a] == "S" and i - 3 >= 0:
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i + 1][a + 1] == "M" and f[i + 2][a + 2] == "A" and f[i + 3][a + 3] == "S" and i + 3 < len(f) and a + 3 < len(f[i]):
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i - 1][a - 1] == "M" and f[i - 2][a - 2] == "A" and f[i - 3][a - 3] == "S" and i - 3 >= 0 and a - 3 >= 0:
                answer += 1
        except IndexError:
            pass
        try:    
            if f[i][a] == "X" and f[i + 1][a - 1] == "M" and f[i + 2][a - 2] == "A" and f[i + 3][a - 3] == "S" and i + 3 < len(f) and a - 3 >= 0:
                answer += 1
        except IndexError:
            pass
        try:
            if f[i][a] == "X" and f[i - 1][a + 1] == "M" and f[i - 2][a + 2] == "A" and f[i - 3][a + 3] == "S" and i - 3 >= 0 and a + 3 < len(f[i]):
                answer += 1
        except IndexError:
            pass
print(answer)