from collections import Counter
import math

train = "the student reads books the student studies NLP"
test = "the student reads books"

w = train.lower().split()
t = test.lower().split()

uni = Counter(w)
bi = Counter(zip(w,w[1:]))

H = 0
for i in range(1,len(t)):
    p = bi[(t[i-1],t[i])] / uni[t[i-1]] \
        if bi[(t[i-1],t[i])] else 0

    if p == 0:
        H = float('inf')
        break

    H += -math.log2(p)

print("Bigram Entropy:", H/(len(t)-1))