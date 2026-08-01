from nltk.stem import PorterStemmer

ps = PorterStemmer()

words=["relational","relation","relate"]

print("-"*45)
print("{:<15}{:<15}".format(
"Original","Final Stem"))
print("-"*45)

for word in words:

    stem=ps.stem(word)

    print("{:<15}{:<15}".format(word,stem))