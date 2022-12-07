encrypted_moves = {"A" : "rock", "B": "paper", "C": "scissors"}
outcome = {"X": 0, "Y": 3, "Z": 6}
points = {"rock": 1, "paper": 2, "scissors": 3}
who_wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
rounds = []
file = open("input.txt", "r")
for line in file:
    row = []
    for move in line.split(" "):
        row.append(move.replace("\n", ""))
    rounds.append(row)

total_score = 0
for round_moves in rounds:
    opponent_move = encrypted_moves[round_moves[0]]
    round_outcome = outcome[round_moves[1]]
    round_score = round_outcome
    if (round_outcome == 3):
        round_score += points[opponent_move]
    elif (round_outcome == 6):
        round_score += points[{i for i in who_wins if opponent_move == who_wins[i]}.pop()]
    else:
        round_score += points[who_wins[opponent_move]]
    total_score += round_score
print(total_score)