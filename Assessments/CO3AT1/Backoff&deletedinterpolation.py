from collections import Counter

text = "the student is intelligent the student likes python"
w = text.split()

uni = Counter(w)
bi = Counter(zip(w,w[1:]))
tri = Counter(zip(w,w[1:],w[2:]))
total = len(w)

query = input("Enter 2 words: ").lower().split()
a,b = query

def U(x): return uni[x]/total
def B(x,y): return bi[(x,y)]/uni[x] if uni[x] else 0
def T(x,y,z): return tri[(x,y,z)]/bi[(x,y)] if bi[(x,y)] else 0

best = {}
for x in uni:
    # Backoff
    p = T(a,b,x) or B(b,x) or U(x)

    # Deleted interpolation
    ip = .2*U(x) + .3*B(b,x) + .5*T(a,b,x)

    best[x] = (p,ip)

print("Predictions:")
for word, values in sorted(best.items(),
                           key=lambda x:x[1][1], reverse=True):
    print(word, values)