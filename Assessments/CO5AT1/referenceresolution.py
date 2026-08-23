text = "Ravi met Arun at the library. He borrowed a book and later returned it."

entities = ["Ravi", "Arun", "book"]

resolved = text.replace("He", "Ravi").replace(" it", " the book")

print("Original:", text)
print("Resolved:", resolved)

print("\nHe -> Ravi")
print("it -> book")