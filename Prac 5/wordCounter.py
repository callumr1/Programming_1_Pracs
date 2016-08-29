
text = str(input("Enter a sentence: "))

wordList = []
wordCount = {}

while text != "":
    wordList = text.split()

    for word in wordList:
        wordCount[word] = (wordList.count(word))
    for word, count in wordCount.items():
        print ("{:<5} : {}".format(word, count))

    break