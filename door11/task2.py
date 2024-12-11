from collections import defaultdict

with open("input.txt", "r") as a:
    f = [int(i) for i in a.read().split()]
a.close()

f = [321, 123]

dict = {}
for b in f:
    dict[b] = 1
print(dict)



def check(a):
    temp = defaultdict(int)
    for i in a:
        count = a[i]
        if i == 0:
            temp[1] += count
        elif len(str(i)) % 2 == 0:
            length = len(str(i))//2
            l = int(str(i)[:length])
            r = int(str(i)[length:])
            temp[l] += count
            temp[r] += count
        else:
            temp[i*2024] += count
    return temp

for i in range(75):
    dict = check(dict)
print(sum([dict[i] for i in dict]))