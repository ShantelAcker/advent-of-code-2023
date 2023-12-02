numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

lines = []
pairs = []
output = 0

with open("input.txt", "r") as input:
    # print(input.readline())
    for line in input:
        lines.append(line.strip())

def convert_word_to_num(word):
    for i in range(len(words)):
        if word == words[i]:
            word = numbers[i]
            break
    return word

for x in range(len(lines)):
    num_1 = ""
    num_2 = ""
    pair = ""
    buffer = ""
    
    # finding first number
    for i in lines[x]:    
        buffer += i    
        for word in words:
            if word in buffer:
                buffer = word
                break
        for num in numbers:
            if num in buffer:
                buffer = num
                break
        if buffer in words or buffer in numbers:
            break
    num_1 = convert_word_to_num(buffer)
    # print(num_1)
    
    # finding second number
    buffer = ""
    for j in reversed(lines[x]):
        buffer += j
        buffer_2 = buffer[::-1]
        for word in words:
            if word in buffer_2:
                buffer = word
                break
        for num in numbers:
            if num in buffer_2:
                buffer = num
                break
        if buffer in numbers or buffer in words:
            break
    num_2 = convert_word_to_num(buffer)
    
    pair = num_1 + num_2
    pairs.append(pair)

for i in pairs:
    output += int(i)

print(output)