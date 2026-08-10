from collections import Counter
import re

text = """The student is intelligent.
The student is hardworking.
The student likes Python.
The teacher is intelligent."""

sents = [re.findall(r'\w+', s.lower()) for s in text.split('.') if s.strip()]

uni = Counter(w for s in sents for w in s)
bi = Counter((a,b) for s in sents for a,b in zip(s,s[1:]))
tri = Counter((a,b,c) for s in sents for a,b,c in zip(s,s[1:],s[2:]))

n = int(input("Enter N (1/2/3): "))
query = input("Enter sentence: ").lower().split()

scores = {}
for w in uni:
    if n == 1:
        p = uni[w] / sum(uni.values())
    elif n == 2:
        p = bi[(query[-1],w)] / uni[query[-1]] if uni[query[-1]] else 0
    else:
        p = tri[(query[-2],query[-1],w)] / bi[(query[-2],query[-1])] \
            if bi[(query[-2],query[-1])] else 0
    scores[w] = p

print("Top 5:", sorted(scores.items(), key=lambda x:x[1], reverse=True)[:5])
print("Unseen probability:", 0)
