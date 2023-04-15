# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 00:41:38 // 4/14 Points (4, 10) [TLE]

caseCount = int(input())
for i in range(1, caseCount + 1):
    COLLISION = False
    weights = list(map(int, input().split()))
    wordCount = int(input())
    words = []
    ciphers = []
    for word in range(wordCount):
        words.append(input())

    def convertToCipher (word, weights):
        newWord = ""
        for char in range(len(word)):
            newWord += str(weights[ord(word[char].lower())-97])
        return newWord
    
    for word in words:
        if not COLLISION:
            newWord = convertToCipher(word, weights)
            if newWord in ciphers:
                COLLISION = True
            else:
                ciphers.append(newWord)

    if COLLISION:
        result = "YES"
    else:
        result = "NO"
    print("Case #{}: {}".format(i, result))