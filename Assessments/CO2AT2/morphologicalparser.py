words = ["disagree", "agreement", "agreeable"]

print("-"*90)
print("{:<12}{:<8}{:<10}{:<10}{:<15}{:<20}".format(
"Word","Prefix","Root","Suffix","Type","Meaning"))
print("-"*90)

for word in words:

    if word=="disagree":
        prefix="dis"
        root="agree"
        suffix="-"
        typ="Derivational"
        meaning="Opposite"

    elif word=="agreement":
        prefix="-"
        root="agree"
        suffix="ment"
        typ="Derivational"
        meaning="State of agreeing"

    else:
        prefix="-"
        root="agree"
        suffix="able"
        typ="Derivational"
        meaning="Capable of agreeing"

    print("{:<12}{:<8}{:<10}{:<10}{:<15}{:<20}".format(
        word,prefix,root,suffix,typ,meaning))