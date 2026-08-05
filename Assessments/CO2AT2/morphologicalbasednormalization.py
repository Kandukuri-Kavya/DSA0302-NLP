words=["govern","government","governance"]

rules={
"govern":("govern","-","Base"),
"government":("govern","ment","Level 1"),
"governance":("govern","ance","Level 1")
}

print("-"*65)
print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
"Word","Root","Affix","Hierarchy","Normalized"))
print("-"*65)

for word in words:
    root,affix,level=rules[word]

    print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
    word,root,affix,level,root))