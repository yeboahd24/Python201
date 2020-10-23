#!usr/bin/env/python3

from datetime import timedelta, date


#
# class DateRangeIterable:
#     """An iterable that contains its own iterator object."""
#
#     def __init__(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date
#         self._present_day = start_date
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._present_day >= self.end_date:
#             raise StopIteration
#         today = self._present_day
#         self._present_day += timedelta(days=1)
#         return today

#
# for days in DateRangeIterable(date(2020, 1, 1), date(2020, 1, 5)):
#     print(days)


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


s1 = DateRangeSequence(date(2018, 1, 1), date(2018, 1, 5))
# for day in s1:
#     print(day)
# print(s1[0])


