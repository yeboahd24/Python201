# gettext works by looking up literal strings in a database of translations and pulling out the
# appropriate translated string. The usual pattern is to bind the appropriate lookup function
# to the name _ (a single underscore character) so that the code is not cluttered with multiple
# calls to functions with longer names.
# The message extraction program, xgettext, looks for messages embedded in calls to the
# catalog lookup functions. It understands different source languages and uses an appropriate
# parser for each. If the lookup functions are aliased, or if extra functions are added, give
# xgettext the names of additional symbols to consider when extracting messages.
# This script has a single message that is ready to be translated.

# The text "This message is in the script." is the message to be substituted from the
# catalog. Fallback mode is enabled, so if the script is run without a message catalog, the
# inline message is printed.

import gettext

# Set up message catalog access.
t = gettext.translation(
'example_domain', 'locale',
fallback=True,
)
_ = t.gettext
print(_('This message is in the script.'))