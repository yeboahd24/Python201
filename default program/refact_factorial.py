from functools import lru_cache

def fact(n: int) -> int:
	"""Not that this can lead to stack overflow

	"""
	if n <=1:
		return 1
	return n * fact(n -1)
print(fact(10))

# refactoring to avoid stack

def prod(int_iter: int) -> int:
	p = 1
	for x in int_iter:
		p*=x
	return p
def fact2(n: int):
	return prod(range(1, n+1))
# print(fact2(1000))


def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

# print(fibo(10))

# reducing it computation complexity with memoization
@lru_cache(128)
def fibo2(n):
	if n <= 1:
		return n
	return fibo2(n - 1) + fibo2(n - 2)
# print(fibo2(128))
