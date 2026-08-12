from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

ps = PorterStemmer()

docs = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]

def stem_text(s):
    return " ".join(ps.stem(w) for w in s.split())

docs = [stem_text(d) for d in docs]

v = CountVectorizer()
X = v.fit_transform(docs)

print("Processed:", docs)
print("Features:", v.get_feature_names_out())
print("Vocabulary size:", len(v.vocabulary_))