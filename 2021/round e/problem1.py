# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 00:49:29 // 0/12 Points (4, 8) [WA]
# Attempt 2: 01:43:52 // 0/12 Points (4, 8) [TLE]
# Attempt 3: 01:53:54 // 0/12 Points (4, 8) [WA]
# Attempt 4: 01:58:22 // 0/12 Points (4, 8) [TLE]
# Attempt 5: 02:35:52 // 4/12 Points (4, 8) [Solved, TLE]
# Attempt 6: 02:45:27 // 4/12 Points (4, 8) [Solved, TLE]
# Attempt 7: 02:48:24 // 4/12 Points (4, 8) [Solved, TLE]
# Can't seem to optimize this one. Forgot to commit previous attempts, but they're saved to the kickstart site I guess.

def checkOK(word):
    if len(word) <= 1:
        return False

    cutoff = int(len(word)/2) + 1
    indLetters = set()

    for char in range(len(word)):
        current = word[char]
        if current in indLetters:
            continue
        if word.count(current) >= cutoff:
            return False
        indLetters.add(current)

    return True

def checkShuffled(word, newWord):
    n = len(word)
    if n != len(newWord):
        return False
    else:
        for i in range(n):
            if word[i] == newWord[i]:
                return False
    return True

def orderSort(word):
    letters = dict()
    newWord = ""
    for idx in range(len(word)):
        if word[idx] in letters:
            letters[word[idx]] += 1
        else:
            letters[word[idx]] = 1
    letters = sorted(letters.items(), key=lambda n: n[1], reverse=True)
    for entry, count in letters:
        newWord += (entry * count)
    return newWord

def rearrangeWord(word):
    def attemptShuffle(oldWord, word):
        size = len(word)
        currentIdx = 0
        newWord = ""
        fails = -1
        while True:
            if fails > size:
                for idx in range(size):
                    char = word[idx]
                    if char != '*':
                        newWord += char
                return newWord
            currentIdx = currentIdx % size
            targetChar = oldWord[currentIdx]
            for i in range(1, size):
                searchIdx = (i + currentIdx) % size
                query = word[searchIdx]
                if query != targetChar and query != '*':
                    newWord += query
                    fails = -1
                    if len(newWord) == size:
                        return newWord
                    word = word[:searchIdx] + '*' + word[searchIdx+1:]
                    break
            currentIdx += 1
            fails += 1

    oldWord = word
    sortedWord = orderSort(word)
    if checkShuffled(oldWord, sortedWord):
        return sortedWord
    else:
        att = 0
        newWord = word
        while True:
            newWord = attemptShuffle(oldWord, newWord)
            if checkShuffled(oldWord, newWord):
                return newWord
            newWord = attemptShuffle(oldWord, (newWord[att:] + newWord[:att]))
            if checkShuffled(oldWord, newWord):
                return newWord
            newWord = attemptShuffle(oldWord, (newWord[::-1]))
            if checkShuffled(oldWord, newWord):
                return newWord
            att += 1

caseCount = int(input())
for caseNum in range(1, caseCount + 1):
    wordOK = True
    result = "IMPOSSIBLE"
    word = str(input()).strip()
    wordOK = checkOK(word)
    
    if wordOK:
        result = rearrangeWord(word)
        assert(checkShuffled(word, result))
    print("Case #{}: {}".format(caseNum, result))