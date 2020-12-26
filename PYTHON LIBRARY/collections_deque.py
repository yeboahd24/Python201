
import collections

# in a list operation
# d = collections.deque('abcdefg')
# print('Deque:', d)
# print('Length:', len(d))
# print('Left end:', d[0])
# print('Right end:', d[-1])
# d.remove('c')
# print('remove(c):', d)


# Add to the right.
d1 = collections.deque()
d1.extend('abcdefg')
print('extend :', d1)
d1.append('h')
print('append :', d1)
# Add to the left.
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

