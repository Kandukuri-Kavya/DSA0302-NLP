words = ["unhappy", "happiness", "happily"]

print("-"*70)
print("{:<12}{:<8}{:<8}{:<10}{:<15}".format(
    "Word","Prefix","Suffix","Root","Type"))
print("-"*70)

for word in words:

    if word=="unhappy":
        prefix="un"
        suffix="-"
        root="happy"
        typ="Derivational"

    elif word=="happiness":
        prefix="-"
        suffix="ness"
        root="happy"
        typ="Derivational"

    else:
        prefix="-"
        suffix="ly"
        root="happy"
        typ="Derivational"

    print("{:<12}{:<8}{:<8}{:<10}{:<15}".format(
        word,prefix,suffix,root,typ))