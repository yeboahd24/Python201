import heapq
from heapq_showtree import show_tree
# from heapq_heapdata import data
data = [19, 9, 4, 10, 11]

# heap = []
# print('random :', data)
# print()
# for n in data:
# 	print('add {:>3}:'.format(n))
# 	heapq.heappush(heap, n)
# 	show_tree(heap)

# print('random :', data)
# heapq.heapify(data)
# print('heapified :')
# show_tree(data)


print('all :', data)
print('3 largest :', heapq.nlargest(3, data))
print('from sort :', list(reversed(sorted(data)[-3:])))
print('3 smallest:', heapq.nsmallest(3, data))
print('from sort :', sorted(data)[:3])