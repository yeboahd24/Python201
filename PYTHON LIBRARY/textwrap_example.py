#!usr/bin/env/python3

import textwrap


sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

# print(textwrap.fill(sample_text, width=60))

# dedented_text = textwrap.dedent(sample_text)
# print('Dedented:')
# print(dedented_text)


# combining dedent with fill
# dedented_text = textwrap.dedent(sample_text).strip()
# for width in [45, 60]:
# 	print('{} Columns:\n'.format(width))

# 	print(textwrap.fill(dedented_text, width=width))
# 	print()

# indenting blog
# dedented_text = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(dedented_text, width=50)
# wrapped += '\n\nSecond paragraph after a blank line.'
# final = textwrap.indent(wrapped, '> ')
# print('Quoted block:\n')
# print(final)


# hanging indent

# dedented_text = textwrap.dedent(sample_text).strip()
# print(textwrap.fill(dedented_text,
# initial_indent='',
# subsequent_indent=' ' * 4,
# width=50,
# ))



# Truncating long text
dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)
print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)
print('\nShortened:\n')
print(shortened_wrapped)
