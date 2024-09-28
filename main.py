import random

import matplotlib.pyplot as plt

ROLLS = 30
GAMES = 100000
JAIL = (10, 0)
RESET = (0, 0)

chance_cards = ["G", "T", "M", "P", "U", "S", "U", "J", "K", "B"] + ["0"] * 6
community_cards = ["G", "J"] + ["0"] * 14

double_counter = 0
current_position = 0

counter = {i: 0 for i in range(40)}

for x in range(GAMES):
    random.shuffle(chance_cards)
    random.shuffle(community_cards)
    (current_position, double_counter) = RESET
    for y in range(ROLLS):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        if die1 == die2:
            double_counter += 1
        else:
            double_counter = 0

        if double_counter >= 3:
            (current_position, double_counter) = JAIL
        else:
            current_position = (current_position + die1 + die2) % 40

            if current_position in [7, 22, 36]:
                card = chance_cards.pop()
                chance_cards.insert(0, card)
                match card:
                    case "G":
                        current_position = 0
                    case "T":
                        current_position = 24
                    case "M":
                        current_position = 39
                    case "P":
                        current_position = 11
                    case "K":
                        current_position = 5
                    case "B":
                        current_position = (current_position - 3) % 40
                    case "J":
                        (current_position, double_counter) = JAIL
                    case "S":
                        match current_position:
                            case 7:
                                current_position = 15
                            case 22:
                                current_position = 25
                            case 36:
                                current_position = 5
                    case "U":
                        match current_position:
                            case 7 | 36:
                                current_position = 12
                            case 22:
                                current_position = 28

            if current_position in [2, 17, 33]:
                card = community_cards.pop()
                community_cards.insert(0, card)
                match card:
                    case "G":
                        current_position = 0
                    case "J":
                        (current_position, double_counter) = JAIL

            if current_position == 30:
                (current_position, double_counter) = JAIL

        counter[current_position] += 1

print("Simulated {} games each with {} rolls".format(GAMES, ROLLS))
print("|--------------|")
print("| PROP | FREQ  |")
print("|--------------|")
for key, val in counter.items():
    print("| {:<4} | {:<4.2f}% |".format(key, (val / (ROLLS * GAMES)) * 100))
print("|--------------|")
