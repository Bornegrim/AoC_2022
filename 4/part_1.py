elf_pairs = []
file = open("4/input.txt", "r")
for line in file:
    row = line.strip('\n').split(',')
    elf_pairs.append(row)

total = 0
for elf_pair in elf_pairs:
    first_elf = elf_pair[0].split('-')
    second_elf = elf_pair[1].split('-')
    if(int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])):
        total += 1
    elif(int(second_elf[0]) <= int(first_elf[0]) and int(second_elf[1]) >= int(first_elf[1])):
        total += 1
print(total)