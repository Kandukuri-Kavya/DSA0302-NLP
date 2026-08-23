sentence = "The boy is playing football."

interlingua = {
    "action": "play",
    "agent": "boy",
    "object": "football",
    "tense": "present",
    "aspect": "progressive"
}

candidates = {
    "Le garçon joue au football.": 0.92,
    "Le garçon joue le football.": 0.54,
    "Le garçon jouer football.": 0.21
}

best = max(candidates, key=candidates.get)

print("Source:", sentence)
print("Interlingua:", interlingua)

print("\nCandidates:")
for text, score in candidates.items():
    print(text, "->", score)

print("\nFinal Translation:", best)