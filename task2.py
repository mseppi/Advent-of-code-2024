f = open("input.txt", "r")
left = []
right = []
answer = 0
for x in f:
    split = x.split(" ")
    left.append(split[0])
    right.append(split[3].replace("\n", ""))

right = list(map(int, right))
left = list(map(int, left))

for i in range(len(right)):
    answer+=left[i] * right.count(left[i])

print(answer)