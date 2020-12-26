import hashlib

# getting all hash algorithms
print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(', '.join(sorted(hashlib.algorithms_available))))
