import re

def split_games():
    """get the games from the input and split the results up by game round"""
    lines = []
    rounds = []

    with open("example.txt", "r") as input:
        for line in input:
            lines.append(line)

    for i in range(len(lines)):
        new_line = re.sub("Game\s[0-9]+:", "", lines[i])
        round = new_line.split(";")
        rounds.append(round)

    return rounds

def check_colors():
    """compare the color count in each round in each game"""
    red_count = 12
    blue_count = 14
    green_count = 13
    rounds = split_games()
    game_numbers = []
    output = 0

    colors_regex = re.compile(r"[0-9]+\s[a-z]+", flags=re.IGNORECASE)

    for i in range(len(rounds)):
        possible = True

        for j in range(len(rounds[i])):
            game = re.findall(colors_regex, rounds[i][j])
            
            for k in range(len(game)):
                if "red" in game[k]:
                    if int(game[k][:2]) > red_count:
                        possible = False
                        break
                if "blue" in game[k]:
                    if int(game[k][:2]) > blue_count:
                        possible = False
                        break
                if "green" in game[k]:
                    if int(game[k][:2]) > green_count:
                        possible = False
                        break
                    
        if possible:
            game_numbers.append(i+1)
            output += (i+1)

    # print(game_numbers)
    return(output)

print(check_colors())