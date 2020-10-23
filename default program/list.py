"""Combination of two list"""

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
# print(flat)

# squaring of each cells

squared = [[x**2 for x in row] for row in matrix]
# print(squared)


# getting the timestamp of secondes within a given year

weeks = 13
days = 2
hours = 7
minutes = 53
seconds = 19

t_s = (((weeks*7+days)*24+hours)*60+minutes)*60+seconds
# print(t_s)


'''coverting timestamp into weeks, days, hours, minutes and seconds'''
t_s = 8063599
fields = []
for b in 60, 60, 24, 7:
	t_s, f = divmod(t_s, b)
	fields.append(f)
fields.append(t_s)
print(fields)