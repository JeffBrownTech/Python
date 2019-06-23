# Function version 1 based on initial thought in code challenge
def char_compare(string1, string2):
    found = True
    for char1 in string1:
        print("in string1: " + char1)
        if char1 not in string2:
            found = False
            break
    
    # Continue testing string2 against string1 if everything in string1 was confirmed found in string2
    if found:
        for char2 in string2:
            print("in string2: " + char2)
            if char2 not in string1:
                found = False
                break
    
    return found

print("This should be true: " + str(char_compare('abcd', 'abcd')))
print("This should be true: " + str(char_compare('abcd', 'aabccd')))
print("This should be false: " + str(char_compare('abcde', 'abcd')))
print("This should be false: " + str(char_compare('abcd', 'efgh')))
print("This should be false: " + str(char_compare('abcd', 'abcde')))
print("This should be false: " + str(char_compare('', 'abcd')))
print("This should be false: " + str(char_compare('abcd', '')))

#------------------------------------------------------------------
# Function version 2 is hopefully faster. Idea is to remove characters that have already been tested to shorten runtime
# If both string copies are length 0 at the end, then all characters were found both
def char_compare2(string1, string2):
    string1_copy = string1
    string2_copy = string2

    for char1 in string1:
        if char1 in string2:
            string1_copy = string1_copy.replace(char1, "")
            string2_copy = string2_copy.replace(char1, "")

    if len(string1_copy) == 0 and len(string2_copy) == 0:
        return True
    else:
        return False


print("This should be true: " + str(char_compare2('abcd', 'abcd')))
print("This should be true: " + str(char_compare2('abcd', 'aabccd')))
print("This should be false: " + str(char_compare2('abcde', 'abcd')))
print("This should be false: " + str(char_compare2('abcd', 'efgh')))
print("This should be false: " + str(char_compare2('abcd', 'abcde')))
print("This should be false: " + str(char_compare2('', 'abcd')))
print("This should be false: " + str(char_compare2('abcd', '')))