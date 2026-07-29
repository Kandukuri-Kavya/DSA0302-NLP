import re

text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""

while True:
    print("\n1.Date")
    print("2.Phone")
    print("3.Hashtag")
    print("4.Mention")
    print("5.Prefix")
    print("6.Suffix")
    print("7.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        print(re.findall(r'\d{2}/\d{2}/\d{4}', text))

    elif ch == 2:
        print(re.findall(r'[6-9]\d{9}', text))

    elif ch == 3:
        print(re.findall(r'#\w+', text))

    elif ch == 4:
        print(re.findall(r'@\w+', text))

    elif ch == 5:
        p = input("Enter Prefix: ")
        print(re.findall(r'\b' + p + r'\w*', text))

    elif ch == 6:
        s = input("Enter Suffix: ")
        print(re.findall(r'\b\w*' + s + r'\b', text))

    elif ch == 7:
        break

    else:
        print("Invalid Choice")