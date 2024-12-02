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

sorted_right = sorted(right)
sorted_left = sorted(left)

for i in range(len(sorted_right)):
    answer += abs(sorted_right[i] - sorted_left[i])

print(answer)
