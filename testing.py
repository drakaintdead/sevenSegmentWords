import re

x = input("Enter a word: ")

if (re.search("[gkmtvwxz]", x)):
    print("yes")
else:
    print("no")