def parser(w):
    irregular = {"children":"child", "men":"man",
                 "women":"woman"}

    if w in irregular:
        return irregular[w], "Plural"
    if w.endswith("ies"):
        return w[:-3] + "y", "Plural"
    if w.endswith("es"):
        return w[:-2], "Plural"
    if w.endswith("s"):
        return w[:-1], "Plural"
    return w, "Singular"

words = ["cars", "boxes", "cities", "children"]

for w in words:
    print(w, "->", parser(w))