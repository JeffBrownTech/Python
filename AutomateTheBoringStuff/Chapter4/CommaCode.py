def addCommas(itemList):
    outputString = ''

    for item in range(len(itemList)):
        if itemList[item] == itemList[-1]:
            outputString = outputString + 'and ' + itemList[item]
        else:
            outputString = outputString + itemList[item] + ', '
    
    print(outputString)


theList = ['apples', 'bananas', 'oranges', 'watermelons']
addCommas(theList)

theList = ['bears', 'beets', 'battlestar galactica']
addCommas(theList)

theList = ['football', 'baseball', 'soccer', 'basketball', 'hockey', 'tennis', 'golf']
addCommas(theList)