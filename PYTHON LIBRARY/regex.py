#!usr/bin/env/python3

import re

#The start() and end() methods give the indexes into the string showing where the text
#matched by the pattern occurs.
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
# print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))


# Precompile the patterns.
regexes = [
re.compile(p)
for p in ['this', 'that', 'God', 'word']
]

strings = "In the begining was the word and the word was with God and the word was God"
# text = 'Does this text match the pattern?'
# print('Text: {!r}\n'.format(strings))
# for regex in regexes:
# 	print('Seeking "{}" ->'.format(regex.pattern),end=' ')
# 	if regex.search(strings):
# 		print('match!')
# 	else:
# 		print('no match')


text = 'abbaaabbbbaaaaa'
pattern = 'ab'
# for match in re.findall(pattern, text):
# 	print('Found {!r}'.format(match))



# for match in re.finditer(pattern, text):
# 	s = match.start()
# 	e = match.end()
# 	print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))


# Greedy
# All these are for repetition of words
"""test_patterns(
'abbaabbba',
[('ab*', 'a followed by zero or more b'),
('ab+', 'a followed by one or more b'),
('ab?', 'a followed by zero or one b'),
('ab{3}', 'a followed by three b'),
('ab{2,3}', 'a followed by two to three b')],
)


# Non Greedy

test_patterns(
'abbaabbba',
[('ab*?', 'a followed by zero or more b'),
('ab+?', 'a followed by one or more b'),
('ab??', 'a followed by zero or one b'),
('ab{3}?', 'a followed by three b'),
('ab{2,3}?', 'a followed by two to three b')],
)


'A character set is a group of characters, any one of which can match at that point in the\
pattern. For example, [ab] would match either a or b.'


test_patterns(
'This is some text -- with punctuation.',
[('[a-z]+', 'sequences of lowercase letters'),
('[A-Z]+', 'sequences of uppercase letters'),
('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
)


test_patterns(
'abbaabbba',
[('a.', 'a followed by any one character'),
('b.', 'b followed by any one character'),
('a.*b', 'a followed by anything, ending in b'),
('a.*?b', 'a followed by anything, ending in b')],
)


test_patterns(
'A prime #1 example!',
[(r'\d+', 'sequence of digits'),
(r'\D+', 'sequence of non-digits'),
(r'\s+', 'sequence of whitespace'),
(r'\S+', 'sequence of non-whitespace'),
(r'\w+', 'alphanumeric characters'),
(r'\W+', 'non-alphanumeric')],
)

test_patterns(
r'\d+ \D+ \s+',
[(r'\\.\+', 'escape code')],
)

test_patterns(
'abbaabbba',
[(r'a((a+)|(b+))', 'capturing form'),
(r'a((?:a+)|(?:b+))', 'noncapturing')],
)"""


# text = 'This is some text -- with punctuation.'
# pattern = r'\bT\w+'

# with_case = re.compile(pattern)
# without_case = re.compile(pattern, re.IGNORECASE)

# print('Text:\n {!r}'.format(text))
# print('Pattern:\n {}'.format(pattern))
# print('Case-sensitive:')
# for match in with_case.findall(text):
# 	print(' {!r}'.format(match))
# 	print('Case-insensitive:')
# for match in without_case.findall(text):
# 	print(' {!r}'.format(match))




address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')
candidates = [
u'first.last@example.com',
u'first.last+category@gmail.com',
u'valid-address@mail.example.com',
u'not-valid@example.foo',
]


# for candidate in candidates:
# 	match = address.search(candidate)
# 	print('{:<30} {}'.format(candidate, 'Matches' if match else 'No match'))


word = 'python programming'
pat = re.compile('(?P<python>[\w\S\s]+)')
match = pat.search(word)
print(match)
