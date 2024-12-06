answer = []
direction = "up"
large_number = 10000

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
while 0<=y<len(f) and 0<=x<len(f[0]):
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



def loop(a, b, ini_y, ini_x,):
    new = [row[:] for row in f]
    new[a][b] = "#"
    y, x = ini_y, ini_x
    new[y][x] = "."
    direction = "up"
    visited = set()
    while 0<=y<len(new) and 0<=x<len(new[0]):
        if direction == "up":
            if y-1>=0 and new[y-1][x] == ".":
                y -= 1
            elif y-1>=0 and new[y-1][x] == "#":
                direction = "right"
                if x+1<len(new[0]) and new[y][x+1] == "#":
                    direction = "down"
            else:
                break
        elif direction == "right":
            if x+1<len(new[0]) and new[y][x+1] == ".":
                x += 1
            elif x+1<len(new[0]) and new[y][x+1] == "#":
                direction = "down"
                if y+1<len(new) and new[y+1][x] == "#":
                    direction = "left"
            else:
                break
        elif direction == "down":
            if y+1<len(new) and new[y+1][x] == ".":
                y += 1
            elif y+1<len(new) and new[y+1][x] == "#":
                direction = "left"
                if x-1>=0 and new[y][x-1] == "#":
                    direction = "up"
            else:
                break
        elif direction == "left":
            if x-1>=0 and new[y][x-1] == ".":
                x -= 1
            elif x-1>=0 and new[y][x-1] == "#":
                direction = "up"
                if y-1>=0 and new[y-1][x] == "#":
                    direction = "right"
            else:
                break
        if (y, x, direction) in visited:
            return True
        visited.add((y, x, direction)) 
    return False

for i in range(len(f)):
    if "^" in f[i]: 
        y = i
        x = f[i].index("^")

        break
answer.remove((y, x))
ini_y, ini_x = y, x
final = 0
for a, b in answer:
    if loop(a, b, ini_y, ini_x):
        final += 1


print(final)

