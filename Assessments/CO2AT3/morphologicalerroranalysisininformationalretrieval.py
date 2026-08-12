from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["watches", "watching", "washable",
         "washer", "washed"]

for w in words:
    print(w, "->", ps.stem(w))