import random

import matplotlib.pyplot as plt

chance_cards = ["GO", "TS", "MF", "PM", "NS",
                "NS", "NU", "JL", "KC", "B3"] + 6 * [""]
community_cards = ["GO", "JL"] + [""] * 14

random.shuffle(chance_cards)
random.shuffle(community_cards)

double_counter = 0
current_position = 0

counter = {i: 0 for i in range(40)}
turns = 100
games = 100000

for x in range(games):
    for y in range(turns):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        if die1 == die2:
            double_counter += 1
        else:
            double_counter = 0
        if double_counter >= 3:
            current_position = 10
            double_counter = 0
        else:
            current_position = (current_position + die1 + die2) % 40

            if current_position in [7, 22, 36]:
                card = chance_cards.pop()
                chance_cards.insert(0, card)
                match card:
                    case "GO":
                        current_position = 0
                    case "TS":
                        current_position = 24
                    case "MF":
                        current_position = 39
                    case "PM":
                        current_position = 11
                    case "KC":
                        current_position = 5
                    case "B3":
                        current_position = (current_position - 3) % 40
                    case "JL":
                        current_position = 10
                        double_counter = 0
                    case "NS":
                        if current_position == 7:
                            current_position = 15
                        elif current_position == 22:
                            current_position = 25
                        else:
                            current_position = 5
                    case "NU":
                        if current_position == 7 or current_position == 36:
                            current_position = 12
                        else:
                            current_position = 28

            if current_position in [2, 17, 33]:
                card = community_cards.pop()
                community_cards.insert(0, card)
                match card:
                    case "GO":
                        current_position = 0
                    case "JL":
                        current_position = 10
                        double_counter = 0

            if current_position == 30:
                current_position = 10
                double_counter = 0

        counter[current_position] += 1

# text rerpr
for k, v in counter.items():
    print(k, " : ", (v / (games * turns)) * 100)
# GUI repr
keys = list(counter.keys())
values = list(counter.values())
plt.bar(keys, values)
plt.xlabel("Square")
plt.ylabel("Frequency")
plt.title("Monopy game square chances")
plt.show()
