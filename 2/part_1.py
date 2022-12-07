encrypted = {"rock" : ["A", "X"], "paper": ["B", "Y"], "scissors": ["C", "Z"]} 
points = {"rock": 1, "paper": 2, "scissors": 3}
who_wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
rounds = []
file = open("test-input.txt", "r")
for line in file:
    row = []
    for move in line.split(" "):
        row.append(move.replace("\n", ""))
    rounds.append(row)

total_score = 0
for round in rounds:
    opponent_move = {i for i in encrypted if round[0] in encrypted[i]}.pop()
    my_move = {i for i in encrypted if round[1] in encrypted[i]}.pop()
    round_score = points[my_move]
    if (opponent_move == my_move):
        round_score += 3
    elif (who_wins[my_move] == opponent_move):
        round_score += 6
    total_score += round_score
print(total_score)