# global state
output = 0
lines = []
symbols_list = []
numbers_map = {}

with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip())

def join_numbers(numbers_list):
    """join seprated number indexes into a single list for each number"""
    buffer = []
    new_numbers_list = []
    for i, x in enumerate(numbers_list):
        buffer.append(x)
        if i+1 == len(numbers_list):
            new_numbers_list.append(buffer)
            break
        if numbers_list[i+1] != x+1:
            new_numbers_list.append(buffer)
            buffer = []
    return new_numbers_list

def create_maps():
    """create maps that store the indexes of valid symbols and numbers separately"""
    for i, x in enumerate(lines):
        # symbols_list = []
        numbers_list = []
        for j, y in enumerate(lines[i]):
            if not (y.isalpha() or y.isdigit() or y == "."):
                symbols_list.append({i:j})
            if y.isdigit():
                numbers_list.append(j)
        if numbers_list:
            numbers_list = join_numbers(numbers_list)
            numbers_map[i] = numbers_list

create_maps()

for i, x in numbers_map.items():
    for j, y in enumerate(x): 
        potentials = []
        symbol_found = False
        for k, z in enumerate(y):            
            top_left = {i-1: z-1}
            top_middle = {i-1: z}
            top_right = {i-1: z+1}
            left = {i: z-1}
            right = {i: z+1}
            bottom_left = {i+1: z-1}
            bottom_middle = {i+1: z}
            bottom_right = {i+1: z+1}
            
            potentials = [top_left, top_middle, top_right, left, right, bottom_left, bottom_middle, bottom_right]

            for potential in potentials:
                if potential in symbols_list and not symbol_found:
                    num = ""
                    for index in y:
                        num += str(lines[i][index])
                    output += int(num)
                    symbol_found = True
print(output)