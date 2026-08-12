from nltk.stem import PorterStemmer

ps = PorterStemmer()

text = """
The organization organized a meeting.
Students are studying science.
Workers are working quickly.
The government announced new policies.
"""

words = text.lower().split()

for word in words:
    word = word.strip(".,")
    print(word, "->", ps.stem(word))