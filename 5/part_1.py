test_creates = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
real_creates = [['V', 'C', 'W', 'L', 'R', 'M', 'F', 'Q'], ['L', 'Q', 'D'], ['B', 'N', 'C', 'W', 'G', 'R', 'S', 'P'], ['G', 'Q', 'B', 'H', 'D', 'C', 'L'], ['S', 'Z', 'F', 'L', 'G', 'V'], ['P', 'N', 'G', 'D'], ['W', 'C', 'F', 'V', 'P', 'Z', 'D'], ['S', 'M', 'D', 'P', 'C'], ['C', 'P', 'M', 'V', 'T', 'W', 'N', 'Z']]
creates = real_creates
moves = []
file = open("5/input.txt", "r")
for line in file:
    row = line.strip('\n').replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
    moves.append(row)

for move in moves:
    amount = int(move[0])
    from_idx = int(move[1]) - 1
    to_idx = int(move[2]) - 1
    creates_to_move = creates[from_idx][:amount]
    for create_to_move in creates_to_move:
        creates[to_idx].reverse()
        creates[to_idx].append(create_to_move)
        creates[to_idx].reverse()
        creates[from_idx].pop(0)
        
    
    
for create in creates:
    print(create[0])