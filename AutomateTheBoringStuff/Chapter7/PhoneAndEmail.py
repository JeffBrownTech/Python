#! python3
# PhoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # telephone prefix
    (\s|-|\.)                       # separator
    (\d{4})                         # line number
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)   
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,8})   # top-level domain (.com, .net, etc)
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    if groups[1] == '':                                         # Checks for no area code
        phoneNum = '-'.join([groups[3], groups[5]])             # Joins telephone prefix and line number by dashes
    elif groups[1][0] == '(':                                   # Check for parenthesis in first character of area code
        phoneNum = '-'.join([groups[3], groups[5]])             # Join telephone prefix and line number by dashes
        phoneNum = ' '.join([groups[1], phoneNum])              # Join area code in parenthesis to phone number with a space
    else:                                                       # All other phone numbers with area code and dashes
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # Join all three parts by dashes
    if groups[8] != '':                                         # Contains extension
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
