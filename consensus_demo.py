

import random

# created 3 delegates with random power, stake, votes (0-100)
# bcos the score average in multiple running was low, i increased the random from 0-100 to 25-100, but not votes
delegates = [
    {
        "name": "Delegate A",
        "power": random.randint(25, 100),
        "stake": random.randint(25, 100),
        "votes": random.randint(0, 100),
    },
    {
        "name": "Delegate B",
        "power": random.randint(25, 100),
        "stake": random.randint(25, 100),
        "votes": random.randint(0, 100),
    },
    {
        "name": "Delegate C",
        "power": random.randint(25, 100),
        "stake": random.randint(25, 100),
        "votes": random.randint(0, 100),
    },
]

# calculate total score for each delegate (power + stake + votes)
# i implemented score as it is the most brute force or direct way to see which delegate stand out in all
# 3 categories, so i put score , now whichever score is highest, that delegate would be selected
for d in delegates:
    d['total_score'] = d['power'] + d['stake'] + d['votes']

# delegate with highest score
winner = max(delegates, key=lambda x: x['total_score'])

print("Delegates Details (Power, Stake, Votes)")
for d in delegates:
    print(f"{d['name']}: Power={d['power']}, Stake={d['stake']}, Votes={d['votes']}, Total Score={d['total_score']}")

print("\nVoters cast votes:")
for d in delegates:
    # votes count ke hisaab se print delegate name multiple times
    for _ in range(d['votes']):
        print(d['name'])

print(f"\nSelected Delegate: {winner['name']} with highest total score {winner['total_score']}")
print("Selection logic: Delegate with highest combined score (power + stake + votes) is chosen.")
