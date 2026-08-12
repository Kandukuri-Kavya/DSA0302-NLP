from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["infection", "infectious", "infected", "infect",
         "infections", "infecting"]

for w in words:
    print(w, "->", ps.stem(w))