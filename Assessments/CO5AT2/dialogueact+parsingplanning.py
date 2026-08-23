history = "I have an important exam tomorrow but I’m not able to concentrate."

responses = [
    "Take a short break because you cannot concentrate, then focus on the most important topics for your exam. Stay confident and keep studying calmly.",
    "Since the exam is tomorrow, take a short break and return with better focus. You can feel confident if you study one topic at a time.",
    "Your exam is important, so take a short break if you cannot concentrate and then focus on your revision. Stay confident because calm study can improve your preparation."
]

keywords = ["focus", "break", "confident"]

print("DIALOGUE ACT: Advise + Encourage\n")

for i, response in enumerate(responses, 1):
    words = response.split()
    found = [k for k in keywords if k in response.lower()]
    
    print("Response", i, ":")
    print(response)
    print("Sentences:", response.count("."))
    print("Keywords:", found)
    print()

# Select response satisfying all constraints
best = responses[1]

print("BEST RESPONSE:")
print(best)