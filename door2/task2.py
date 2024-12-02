
def is_safe(lst):
        if lst[0] > lst[1]:    
            for a in range(len(lst) - 1):
                if lst[a] - lst[a + 1] > 3 or lst[a] - lst[a + 1] <= 0:
                    return False
            return True
        elif lst[0] < lst[1]:
            for a in range(len(lst) - 1):
                if lst[a + 1] - lst[a] > 3 or lst[a + 1] - lst[a] <= 0:
                    return False
            return True
        else:
            return False 


f = open("input.txt", "r")
answer = 0
for i in f:
    safe = False
    i = i.split(" ")
    i[-1] = i[-1].replace("\n", "")
    i = list(map(int, i))
    for e in range(len(i)):
        lst = [i[j] for j in range(len(i)) if j != e]
        if is_safe(lst):
            safe = True
            break
    if safe:
        answer += 1
print(answer)