#!user/bin/env python3

"""Using walrus := to simplify our function"""

p = 0
for n in range(0, 20_000):   # without walrus 
	term = (1/(2*n+1))**2
	if term >= 0.000_000_001:
		p = p + term
# print(p)


q = 0
 
for n in range(0, 20_000):
	if (term := (1/(2*n+1))**2) >=0.000_000_001: # with walrus
		q = q + term
	else :
		break
# print(q)


data = [11,13,17,19,23,29]
total = 0
# for d in data:
# 	total+=d
# # print(total)

running_sum = [total := total + d for d in data]
# print(total)

