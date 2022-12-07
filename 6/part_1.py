file = open("6/test-input.txt", "r")
data_buffer = ""
for line in file:
    data_buffer += line

result = []
for idx, char in enumerate(data_buffer):
    if char not in result:
        result.append(char)
    else:
        print(result)
        idx_to_remove = result.index(char)
        result = result[idx_to_remove + 1:]
        print(result)
    if len(result) >= 4:
        print(idx + 1)
        break