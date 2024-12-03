import re

answer = 0
with open("input.txt", "r") as a:
    f = a.read()

pattern = re.compile(r'mul\(\d+,\s*\d+\)')
matches = pattern.findall(f)

for match in matches:
    match = match.replace("mul(", "")
    match = match.replace(")", "")
    match = match.split(",")
    answer += int(match[0]) * int(match[1])

print(answer)