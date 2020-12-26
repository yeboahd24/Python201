# The prmonth() method is a simple function that produces the formatted text output for a
# month.

import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# c.prmonth(2017, 7)


# The example configures TextCalendar to start weeks on Sunday, following the
#  U.S. convention. The default is to use the European convention of starting a week on Monday. 
# The example produces the following output.


cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2017, 2, 1, 1, 3))
