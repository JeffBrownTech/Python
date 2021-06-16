#! python3
# SSNAndCreditCardNumbers.py - Finds Social Security Numbers and Credit Card numbers and mask them

# Current issue: two different regex patterns to identify with and without dashes.
# Doing this in order to perform accurate * replacements in string.
# Need a more dynamic way to do this.

# Example Text:
# The loan applicant's SSN is 444-55-9876. The cosigner is 444392234. They plan on paying with 4444-3456-2234-6799 or 4859382763384569 as a backup.

import pyperclip, re

ssnDashRegex = re.compile(r'''(
    (\d{3}-\d{2})    # Match XXX-XX
    (?=-\d{4})       # Match -XXXX
)''', re.VERBOSE)

ssnNoDashRegex = re.compile(r'(\d{5})(?=\d{4})')

ccDashRegex = re.compile(r'''(
    ((\d{4}-){3})    # Match XXXX- three time
    (?=\d{4})        # Match last four
)''', re.VERBOSE)

ccNoDashRegex = re.compile(r'(\d{12})(?=\d{4})')

# Find matches in clipboard text
text = str(pyperclip.paste())

# Print original text
print(text)

# Perform redaction and print new text
text = ssnDashRegex.sub(r'***-**', text)
text = ssnNoDashRegex.sub(r'*****', text)
text = ccDashRegex.sub(r'****-****-****-', text)
text = ccNoDashRegex.sub(r'************', text)
print(text)