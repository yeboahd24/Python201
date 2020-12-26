import multiprocessing

def worker(num): # spawing is where by we give an args to thread or multiprocessing
	"""thread worker function"""
	print('Worker:', num)
if __name__ == '__main__':
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=worker, args=(i,))
		jobs.append(p)
		p.start()