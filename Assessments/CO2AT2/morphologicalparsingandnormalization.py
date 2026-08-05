words=["activate","activation","reactivation"]

print("-"*90)
print("{:<15}{:<8}{:<12}{:<10}{:<20}{:<12}".format(
"Word","Prefix","Root","Suffix","Sequence","Normalized"))
print("-"*90)

for word in words:

    if word=="activate":
        prefix="-"
        root="activate"
        suffix="-"
        seq="Base"

    elif word=="activation":
        prefix="-"
        root="activate"
        suffix="ion"
        seq="activate→activation"

    else:
        prefix="re"
        root="activate"
        suffix="ion"
        seq="activate→reactivation"

    print("{:<15}{:<8}{:<12}{:<10}{:<20}{:<12}".format(
    word,prefix,root,suffix,seq,root))