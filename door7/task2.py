answer = 0

with open("input.txt", "r") as a:
    f = a.readlines()
f = [i.replace("\n", "") for i in f]
list = []
for i in f:
    value, numbers = i.split(":")
    list.append((int(value), [*map(int, numbers.strip().split())]))

for value, numbers in list:
    list2 = [numbers.pop(0)]
    while numbers:
        a = numbers.pop(0)
        list3 = []
        for i in list2:
            list3.append(i + a)
            list3.append(i * a)
            list3.append(int(str(i) + str(a)))
        list2 = list3
    if value in list2:
        answer += value
print(answer)