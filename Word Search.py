from datetime import datetime
start = datetime.now()

rowCount = 9
colCount = 9
goRight = [
    [row*colCount+col for col in range(colCount)] for row in range(rowCount)]
goLeft = [list(reversed(positions)) for positions in goRight]
goDown = [
    [row*colCount+col for row in range(rowCount)] for col in range(colCount)]
goUp = [list(reversed(positions)) for positions in goDown]
goDownRight = [[row*colCount+row+col for row in range(min(rowCount, colCount-col))] for col in range(colCount-1)] \
    + [[(row+col)*colCount+col for col in range(min(rowCount-row, colCount))]
       for row in range(1, rowCount-1)]
goUpLeft = [list(reversed(positions)) for positions in goDownRight]
goDownLeft = [[row*colCount-row+col for row in range(min(rowCount, col+1))] for col in range(1, colCount)] \
    + [[(row+1+col)*colCount-1-col for col in range(min(rowCount-row, colCount))]
       for row in range(1, rowCount-1)]
goUpRight = [list(reversed(positions)) for positions in goDownLeft]

segments = [("horizontally going right",    segment) for segment in goRight] \
    + [("horizontally going left",     segment) for segment in goLeft] \
    + [("vertically going down",       segment) for segment in goDown] \
    + [("vertically going up",         segment) for segment in goUp] \
    + [("diagonally going down-right", segment) for segment in goDownRight] \
    + [("diagonally going up-left",    segment) for segment in goUpLeft] \
    + [("diagonally going down-left",  segment) for segment in goDownLeft] \
    + [("diagonally going up-right",   segment) for segment in goUpRight]

# Generate the letter matrix as a simple list:

letter_array = ['M', 'V', 'G', 'L', 'I', 'X', 'A', 'P', 'E',
                'J', 'H', 'B', 'X', 'E', 'E', 'N', 'P', 'P',
                'H', 'K', 'T', 'T', 'H', 'B', 'S', 'W', 'Y',
                'R', 'W', 'A', 'I', 'N', 'U', 'Y', 'Z', 'H',
                'P', 'P', 'F', 'X', 'R', 'D', 'Z', 'K', 'Q',
                'T', 'P', 'N', 'L', 'Q', 'O', 'Y', 'J', 'Y',
                'A', 'N', 'H', 'A', 'P', 'F', 'G', 'B', 'G',
                'H', 'X', 'M', 'S', 'H', 'W', 'Y', 'L', 'Y',
                'U', 'J', 'F', 'J', 'H', 'R', 'S', 'O', 'A']
# Import word dictionary from .txt file
word_list1 = open("dictionary1.txt").readlines()
word_list = []
for elem in word_list1:
    word_list.extend(elem.strip().split('\n'))

segmentStrings = [(direction, positions, "".join(
    map(lambda i:letter_array[i], positions))) for direction, positions in segments]

# check for words ...

for word in word_list:
    for direction, positions, segmentString in segmentStrings:
        startPos = segmentString.find(word)  # see note below
        if startPos < 0:
            continue
        wordPositions = positions[startPos:][:len(word)]
        gridPositions = [(position // colCount, position % colCount)
                         for position in wordPositions]
        print(word, "found\t starting at",
              wordPositions[0], direction, gridPositions)
        break  # don't break here if you want to find all matches
print("Gone through dictionary with total words of ", "(",
      len(word_list), ")", "and Program Runtime is:", datetime.now()-start)
