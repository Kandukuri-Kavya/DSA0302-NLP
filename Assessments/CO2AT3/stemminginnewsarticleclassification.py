from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["organization", "organizer", "organizing",
         "organized", "organization's"]

for w in words:
    print(w, "->", ps.stem(w))