with open("lr6/numbers_input.txt", "r", encoding="utf-8") as f:
    numbers = f.readlines()
    numbers = [int(x) for line in numbers for x in line.split()]

numbers.sort()

with open("lr6/numbers_output.txt", "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")
