names = ["Jeremy", "Kady", "Oliva", "Jason", "Adam"]
roles = ["Scribe", "Facilitator"]

for week in range(1, 7):
    scribe = names[week % len(names)]
    facilitator = names[(week + 1) % len(names)]
    print(f"Week {week}:")
    print(f"Scribe: {scribe}")
    print(f"Facilitator: {facilitator}")
    print()