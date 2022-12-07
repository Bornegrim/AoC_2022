rucksack_groups = []
file = open("3/input.txt", "r")
for idx, line in enumerate(file):
    if (idx % 3) == 0:
        rucksack_groups.append([])
    rucksack_groups[len(rucksack_groups) - 1].append(line.strip("\n"))
    
total = 0
for rucksack_group in rucksack_groups:
    first_rucksack = rucksack_group[0]
    second_rucksack = rucksack_group[1]
    third_rucksack = rucksack_group[2]
    common_item = next((item for idx, item in enumerate(first_rucksack) if first_rucksack[idx] in second_rucksack and first_rucksack[idx] in third_rucksack))
    if common_item.isupper():
        total += (ord(common_item) - 64 + 26)
    else:
        total += (ord(common_item) - 96)
print(total)