numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lines = []
pairs = []
output = 0

with open("input.txt", "r") as input:
    # print(input.readline())
    for x in input:
        lines.append(x)

for x in range(len(lines)):
    tmp = ""
    for y in lines[x]:
        if y in numbers:
            tmp += y
            break
    for z in reversed(lines[x]):
        if z in numbers:
            tmp += z
            break
    pairs.append(tmp)

for i in pairs:
    output += int(i)

print(output)