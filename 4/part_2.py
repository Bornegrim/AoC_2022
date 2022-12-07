elf_pairs = []
file = open("4/input.txt", "r")
for line in file:
    row = line.strip('\n').split(',')
    elf_pairs.append(row)

total = 0
for elf_pair in elf_pairs:
    first_elf = elf_pair[0].split('-')
    first_elf_range = [*range(int(first_elf[0]), int(first_elf[1]) + 1)]
    second_elf = elf_pair[1].split('-')
    second_elf_range = [*range(int(second_elf[0]), int(second_elf[1]) + 1)]
    if len(list(set(first_elf_range) & set(second_elf_range))) > 0:
        total += 1
print(total)