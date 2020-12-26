#!usr/bin/env/python3
import time

# One of the core functions of the time module is time(), which returns the number of seconds
# since the start of the “epoch” as a floating-point value.

print('The time is:', time.time())

# The float representation is highly useful when storing or comparing dates, but less useful
# for producing human-readable representations. For logging or printing times, ctime() can
# be a better choice.

print('The time is :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))