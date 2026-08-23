sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

# Word Sense Disambiguation
if "river" in sentence.lower() and "flooded" in sentence.lower():
    sense = "riverbank"
else:
    sense = "financial bank"

print("Original Sentence:")
print(sentence)

print("\nWord Sense Disambiguation:")
print("bank ->", sense)

# Predicate logic representation
predicates = [
    "bank(b)",
    "river(r)",
    "location(b,r)",
    "storm(s)",
    "flood(b)",
    "after(flood(b),s)",
    "quick_action(a)",
    "saved_by(b,a)"
]

print("\nPredicate Logic:")
for p in predicates:
    print(p)

# Discourse relation
if "but" in sentence.lower():
    relation = "Contrast"
else:
    relation = "Unknown"

print("\nDiscourse Relation:", relation)

# Clear target sentence
paraphrase = (
    "The riverbank flooded after the storm, "
    "but quick action saved the riverbank."
)

print("\nResolved Target Sentence:")
print(paraphrase)

# Simple discourse tree
print("\nRST-STYLE DISCOURSE TREE:")
print("             CONTRAST")
print("             /       \\")
print(" Flooding occurred   Riverbank was saved")
print(" after the storm     by quick action")

# Advantages
print("\nADVANTAGES OF CONSTRAINT-BASED APPROACH:")
print("1. Resolves bank using river and flooding context.")
print("2. Preserves important entities and relations.")
print("3. Maintains the Contrast relation.")
print("4. Reduces semantic ambiguity.")