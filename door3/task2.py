import re

answer = 0
with open("input.txt", "r") as a:
    f = a.read()
pattern = re.compile(r"don't\((.*?)\)do\(\)")

parts = re.split(r"(do\(\)|don't\(\))", f)



handle = True

for i in parts:
    if i == "do()":
        handle = True
    elif i == "don't()":
        handle = False
    else:
        if handle:
            pattern = re.compile(r'mul\(\d+,\s*\d+\)')
            matches = pattern.findall(i)
            for match in matches:
                match = match.replace("mul(", "")
                match = match.replace(")", "")
                match = match.split(",")
                answer += int(match[0]) * int(match[1])


print(answer)