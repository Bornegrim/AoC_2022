rucksacks = []
file = open("3/input.txt", "r")
for line in file:
    row = []
    rucksacks.append([line[:len(line)//2], line[len(line)//2:].strip("\n")])
    
total = 0    
for rucksack in rucksacks:
    first_compartment = rucksack[0]
    second_compartment = rucksack[1]
    common_item = next((item for idx, item in enumerate(first_compartment) if first_compartment[idx] in second_compartment))

    if common_item.isupper():
        total += (ord(common_item) - 64 + 26)
    else:
        total += (ord(common_item) - 96)
print(total)
    