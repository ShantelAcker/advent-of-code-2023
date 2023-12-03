output = 0
lines = []

with open("input.txt", "r") as input:
    for line in input:
        lines.append(line)

for i, x in enumerate(lines):
    games = x.split(":")[1].strip().split("; ")

    red = blue = green = 0
    for game in games:
        for round in game.split(", "):
            num, color = round.split(" ")
            num = int(num)
            if color == "red":
                if num > red:
                    red = num
            if color == "blue":
                if num > blue:
                    blue = num
            if color == "green":
                if num > green:
                    green = num
    power = red * blue * green
    output += power

print(output)