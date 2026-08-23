text = ("John and Mary went to the park. He brought a ball. "
        "She wanted to play with it. The dog chased him excitedly. "
        "Finally, they all went home.")

# Referring expressions and possible antecedents
candidates = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John", "Mary", "dog"]
}

# Apply constraints
resolved = {
    "He": "John",          # gender + coherence
    "She": "Mary",         # gender + coherence
    "it": "ball",          # semantic compatibility
    "him": "John",         # gender + semantic compatibility
    "they": "John, Mary and the dog"
}

print("REFERRING EXPRESSIONS")
for pronoun, ants in candidates.items():
    print(pronoun, "->", ants)

print("\nRESOLUTION")
for pronoun, ant in resolved.items():
    print(pronoun, "->", ant)

# Rewrite paragraph
result = text.replace("He", "John")
result = result.replace("She", "Mary")
result = result.replace("with it", "with the ball")
result = result.replace("chased him", "chased John")
result = result.replace("they all", "John, Mary and the dog")

print("\nRESOLVED DISCOURSE:")
print(result)

print("\nCOREFERENCE CHAINS:")
print("John -> He -> him")
print("Mary -> She")
print("ball -> it")
print("John + Mary + dog -> they")