#saves a textstring to a variabel and prints it t the consol.
phrase = "The older you get, the better you get, unless you’re a banana."
print(phrase)

#splits the text after ever , and prints it t the consol.
numberofwords = phrase.split(",")
for words in numberofwords:
    print(words)

#splits the text after ever word and prints in to the consol.
numberofwords = phrase.split()
for words in numberofwords:
    print(words)