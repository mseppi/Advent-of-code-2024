answer = []
direction = "up"

with open("input.txt", "r") as a:
    f = a.read()
f = f.split("\n")
f = [list(i) for i in f]
for i in range(len(f)):
    if "^" in f[i]:
        y = i
        x = f[i].index("^")
        break

answer.append((y, x))
while 0<=y<=len(f) and 0<=x<=len(f[0]):
    if direction == "up":
        if y-1>=0 and f[y-1][x] == ".":
            y -= 1
        elif y-1>=0 and f[y-1][x] == "#":
            direction = "right"
            x += 1
        else:
            break
    elif direction == "right":
        if x+1<len(f[0]) and f[y][x+1] == ".":
            x += 1
        elif x+1<len(f[0]) and f[y][x+1] == "#":
            direction = "down"
            y += 1
        else:
            break
    elif direction == "down":
        if y+1<len(f) and f[y+1][x] == ".":
            y += 1
        elif y+1<len(f) and f[y+1][x] == "#":
            direction = "left"
            x -= 1
        else:
            break
    elif direction == "left":
        if x-1>=0 and f[y][x-1] == ".":
            x -= 1
        elif x-1>=0 and f[y][x-1] == "#":
            direction = "up"
            y -= 1
        else:
            break
    answer.append((y, x))
answer = set(answer)
print(len(answer))
        
       