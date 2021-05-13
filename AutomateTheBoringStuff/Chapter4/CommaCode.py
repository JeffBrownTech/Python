# Comma Code

# Write a function that takes a list value and returns a string with all the items separated by a comma and space.
# For the last item in the list, add 'and'
# Example input: theList = ['apples', 'bananas', 'oranges', 'watermelons']
# Example output: apples, bananas, oranges, and watermelons

def addCommas(itemList):
    outputString = ''

    for item in range(len(itemList)):
        if itemList[item] == itemList[-1]:
            outputString = outputString + 'and ' + itemList[item]
        else:
            outputString = outputString + itemList[item] + ', '
    
    return outputString


theList = ['apples', 'bananas', 'oranges', 'watermelons']
print(addCommas(theList))

theList = ['bears', 'beets', 'battlestar galactica']
print(addCommas(theList))

theList = ['football', 'baseball', 'soccer', 'basketball', 'hockey', 'tennis', 'golf']
print(addCommas(theList))