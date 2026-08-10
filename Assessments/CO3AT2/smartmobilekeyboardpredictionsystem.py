import math

# Given counts
data = 3
data_science = 3
science_is = 2
science_drives = 1
total = 12

# MLE
p = data_science / data
print("P(science|data) =", p)

# Backoff for unseen "improves"
print("P(improves) =", 0)

# Deleted Interpolation
p3 = 2/3
p2 = 2/3
p1 = 2/total
p = .5*p3 + .3*p2 + .2*p1
print("Interpolated P(is) =", round(p,4))

# Entropy
x, y = .66, .33
H = -(x*math.log2(x) + y*math.log2(y))
print("Entropy =", round(H,4))