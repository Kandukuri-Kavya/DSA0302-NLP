words = ["connected", "connecting", "connection"]

rules = {
    "connected": ("connect", "ed", "Inflectional"),
    "connecting": ("connect", "ing", "Inflectional"),
    "connection": ("connect", "ion", "Derivational")
}

print("-"*60)
print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
    "Word","Root","Suffix","Type","Normalized"))
print("-"*60)

for word in words:
    root, suffix, t = rules[word]
    print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
        word, root, suffix, t, root))