
text = str(input("Enter a sentence: "))

wordCount = {}

wordList = text.split()

for word in wordList:
    wordCount[word] = wordList.count(word)

for word, count in wordCount.items():
    longestWord = max(len(word) for word in wordList)
    print ("{:{}} : {}".format(word, longestWord, count))
