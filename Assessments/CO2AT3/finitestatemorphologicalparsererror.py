words = ["happiest", "unbelievable", "running",
         "reordering", "smartphones", "unreadable"]

suffix = ["est", "able", "ing", "s"]
prefix = ["un", "re"]

for w in words:
    root = w
    for p in prefix:
        if root.startswith(p):
            root = root[len(p):]
    for s in suffix:
        if root.endswith(s):
            root = root[:-len(s)]
    print(w, "->", root)