import nltk

arpabet = nltk.corpus.cmudict.dict()

seasonalWords = set()

isHaiku = False
hasSeasonalWord = False
hasSylNum = False

fileIn = open('seasons.txt')
for line in fileIn:
    seasonalWords.add(line.strip())
fileIn.close()


poem = open('poem.txt')

# keep track of line number so that you can keep track of proper syllable number
lineNum = 1

totalNumSyl = 0

# loop through each line of poem
for line in poem:
    # split line into words
    line = line.split()

    numSyl = 0

    # loop through words in line
    for word in line:
        # check if any words used are seasonal words
        if word.upper() in seasonalWords:
            hasSeasonalWord = True

        # count syllables
        sylList = arpabet[word.lower()][0]
        for syl in sylList:
            if syl[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                numSyl += 1
        # if first or last line and num syllables is 5, add 5 to total syllable count
        if (lineNum == 1 or lineNum == 3) and numSyl == 5:
            totalNumSyl += 5

        # if middle line and numSyl is 7, add 7 to total count
        elif lineNum == 2 and numSyl == 7:
            totalNumSyl += 7

    lineNum += 1
# check total syllables and seasonal words to verify if poem is haiku
if totalNumSyl == 17 and hasSeasonalWord:
    isHaiku = True

poem.close()

if isHaiku:
    print("This poem is a haiku!")




