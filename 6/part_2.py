file = open("6/input.txt", "r")
data_buffer = ""
for line in file:
    data_buffer += line

result = []
for idx, char in enumerate(data_buffer):
    if char in result:
        idx_to_keep = result.index(char) + 1
        result = result[idx_to_keep:] + [char]
    else:
        result.append(char)
    if len(result) >= 14:
        print(idx + 1)
        break
