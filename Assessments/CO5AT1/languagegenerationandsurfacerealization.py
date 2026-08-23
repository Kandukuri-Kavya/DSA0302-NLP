semantic = {
    "action": "buy",
    "agent": "student",
    "object": "book",
    "tense": "past"
}

verb = "bought" if semantic["tense"] == "past" else "buy"

sentence = "The " + semantic["agent"] + " " + verb + " a " + semantic["object"] + "."

print("Semantic Input:", semantic)
print("Generated Sentence:", sentence)