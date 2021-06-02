#! python3
# PhoneAndEmail.py - Finds Web site URLs starting with http:// or https://.

import pyperclip, re

urlRegex = re.compile(r'''(
    http(s)?    # Match http or https
    ://         # Protocol separator
    (\S)+       # Finds any character or digit that is not a space
    [^.]        # Excludes trailing periods (if URL is at end of a sentence)
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

print(urlRegex.findall(text))

for groups in urlRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No Web site URLs found.')
