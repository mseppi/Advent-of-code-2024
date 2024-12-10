from collections import Counter

with open("input.txt", "r") as a:
    f = a.read()
a.close()

list = []
empty = False
id = 0
for i in f:
    if not empty:
        for _ in range(int(i)):
            list.append(id)
        empty = True
        id+=1
    else:
        for _ in range(int(i)):
            list.append(".")
        empty = False

dots = Counter(list)

dot_indices = [i for i, x in enumerate(list) if x == "."]
o = "."
for i in dot_indices:
    if dots["."] == 0:
        break
    while list[-1] == ".":
        list.pop()
        dots["."] -= 1
    if i >= len(list):
        break
    list[i] = list.pop()
    dots[list[i]] -= 1

    
answer = 0
for x, y in enumerate(list):
    answer+=x*y
print(answer)


                    

    

