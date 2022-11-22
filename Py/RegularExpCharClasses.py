import re


pattern = r'.'
text = 'abcdef'

pattern = r'\d'
text = 'FirstWord 1 LastWord'

pattern = r'\D'
text = 'FirstWord 1 LastWord'

pattern = r'\w'
text = 'FirstWord 1 LastWord'

pattern = r'\s'
text = 'FirstWord 1 LastWord'

pattern = r'\S'
text = 'FirstWord 1 LastWord'

pattern = r'\w+'
text = 'FirstWord 1 LastWord'

pattern = r'[4-6]'
text = '123456789'

pattern = r'[4-6]+'
text = '123456789'

pattern = r'[d-f]+'
text = 'abcdefghi'

pattern = r'[a-z0-9]+'
text = 'word!1234?wordandletters'

pattern = r'[a-z0-9]+'
text = 'WORD!1234?wordandletters'

pattern = r'[^aeiou^\s]+'
text = 'The quick brown fox jumps over the lazy dog.'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")