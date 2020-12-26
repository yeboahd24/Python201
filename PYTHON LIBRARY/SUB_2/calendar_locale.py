# To produce a calendar formatted for a locale other than the current default,
#  use LocaleTextCalendar or LocaleHTMLCalendar.


import calendar
c = calendar.LocaleTextCalendar(locale='en_US')
c.prmonth(2017, 7)
print()
c = calendar.LocaleTextCalendar(locale='fr_FR')
c.prmonth(2017, 7)