text = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

relations = [
    ("S1", "S2", "Cause-Effect"),
    ("S2", "S3", "Consequence/Sequence")
]

print("Discourse Structure:")
for r in relations:
    print(r[0], "->", r[1], ":", r[2])

print("\nSentences:")
for i, s in enumerate(text, 1):
    print("S" + str(i) + ":", s)