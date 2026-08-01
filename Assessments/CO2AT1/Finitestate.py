words=["writes","writing","written"]

print("-"*80)
print("{:<10}{:<28}{:<12}{:<10}".format(
"Word","State Transition","Pattern","Root"))
print("-"*80)

for word in words:

    if word=="writes":
        path="Start->write->s->End"
        pattern="Regular"
        root="write"

    elif word=="writing":
        path="Start->write->ing->End"
        pattern="Regular"
        root="write"

    else:
        path="Start->write->written->End"
        pattern="Irregular"
        root="write"

    print("{:<10}{:<28}{:<12}{:<10}".format(
    word,path,pattern,root))