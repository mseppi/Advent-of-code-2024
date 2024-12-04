answer = 0

with open("input.txt", "r") as a:
    f = a.read()
f = f.split("\n")
for i in range(1, len(f)-1):
    for a in range(1, len(f[i])-1):
        if f[i][a] == "A" and f[i+1][a+1] == "M" and f[i-1][a-1] == "S" and f[i-1][a+1] == "M" and f[i+1][a-1] == "S":
            answer += 1
        if f[i][a] == "A" and f[i+1][a+1] == "S" and f[i-1][a-1] == "M" and f[i-1][a+1] == "M" and f[i+1][a-1] == "S":
            answer += 1
        if f[i][a] == "A" and f[i+1][a+1] == "M" and f[i-1][a-1] == "S" and f[i-1][a+1] == "S" and f[i+1][a-1] == "M":
            answer += 1
        if f[i][a] == "A" and f[i+1][a+1] == "S" and f[i-1][a-1] == "M" and f[i-1][a+1] == "S" and f[i+1][a-1] == "M":
            answer += 1
print(answer)