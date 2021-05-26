# Chapter 6
# Table Printer
# Print a list of strings into a well-organized table, each column right-justified.
# Each inner list contains the same number of strings.
# The function would print the following:

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

def printTable(table):
    xLen = len(table)
    yLen = len(table[0])
    colWidths = [0] * xLen

    for column in range(xLen):
        for item in range(len(table[column])):
            currLen = len(table[column][item])
            if currLen > colWidths[column]:
                colWidths[column] = currLen
    
    for y in range(yLen):
        for x in range(xLen):
            print(table[x][y].rjust(colWidths[x]), end=' ')
        print('')
    return

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# tableData = [['Fruits', 'apples', 'watermelon', 'cherries', 'banana'],
#              ['People', 'Alice', 'Bob', 'Carol', 'Michael'],
#              ['Animals', 'anteater', 'cats', 'moose', 'goose'],
#              ['Sports', 'basketball', 'footbal', 'golf', 'hockey']]

printTable(tableData)