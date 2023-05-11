with open("lr6/text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    reversed_line = line[::-1]
    print(reversed_line)
