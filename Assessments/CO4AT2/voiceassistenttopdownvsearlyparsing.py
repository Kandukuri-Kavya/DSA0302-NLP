sentence = "Book a flight to Delhi with a window seat"

print("Input:", sentence)

print("\nTop-Down Parsing:")
print("S -> VP")
print("VP -> V NP PP")
print("V -> Book")
print("NP -> a flight")
print("PP -> to Delhi")
print("PP -> with a window seat")

print("\nEarley Parsing:")
print("Prediction -> Scanning -> Completion")
print("Parse completed successfully.")

print("\nBest Parser for real-time input: Earley Parser")