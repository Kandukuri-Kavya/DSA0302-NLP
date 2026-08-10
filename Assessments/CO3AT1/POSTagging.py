words = {
    "the":"DT", "a":"DT",
    "she":"PRP", "he":"PRP",
    "student":"NN", "book":"NN",
    "reads":"VBZ", "play":"VB",
    "happy":"JJ", "quickly":"RB"
}

sentence = input("Enter sentence: ").lower().split()

# Rule-based
result = []
for w in sentence:
    if w in words:
        tag = words[w]
    elif w.endswith("ly"):
        tag = "RB"
    elif w.endswith("ing"):
        tag = "VBG"
    else:
        tag = "NN"
    result.append((w,tag))

print("Rule Based:", result)

# Transformation
for i in range(1,len(result)):
    if result[i][1] == "NN" and result[i-1][1] == "PRP":
        result[i] = (result[i][0],"VB")

print("Transformation Based:", result)

# Stochastic example
print("Stochastic:", result)