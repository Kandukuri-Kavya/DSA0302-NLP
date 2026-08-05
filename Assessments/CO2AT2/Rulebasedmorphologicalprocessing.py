words = ["analyzing", "analysis", "analytical"]

rules = {
    "analyzing": ("analyze", "ing", "Inflectional"),
    "analysis": ("analyze", "sis", "Derivational"),
    "analytical": ("analyze", "ical", "Derivational")
}

print("-"*65)
print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
    "Word","Root","Affix","Type","Normalized"))
print("-"*65)

for word in words:
    root, affix, typ = rules[word]
    print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
        word, root, affix, typ, root))