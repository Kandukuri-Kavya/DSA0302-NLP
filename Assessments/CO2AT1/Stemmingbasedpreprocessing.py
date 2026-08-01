words=["played","player","playing"]

rules={
"played":("play","ed","Inflectional"),
"player":("play","er","Derivational"),
"playing":("play","ing","Inflectional")
}

print("-"*65)
print("{:<10}{:<10}{:<10}{:<15}{:<10}".format(
"Word","Stem","Affix","Type","Normalized"))
print("-"*65)

for word in words:
    stem,affix,typ=rules[word]

    print("{:<10}{:<10}{:<10}{:<15}{:<10}".format(
    word,stem,affix,typ,stem))