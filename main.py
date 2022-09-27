import re
def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

words = load_words()

longestWords = ["x"]

for x in words:
    if not(re.search("[gkmqvwxzi]", x)):
        if len(x) > len(longestWords[-1]):
            longestWords.clear()
            longestWords.append(x)
        elif len(x) == len(longestWords[-1]):
            longestWords.append(x)

print(longestWords)