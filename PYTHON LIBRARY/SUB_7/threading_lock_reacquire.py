# Normal Lock objects cannot be acquired more than once, even by the same thread. If a lock
# is accessed by more than one function in the same call chain, undesirable side effects may
# occur.

import threading
lock = threading.Lock()
print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# In this case, the second call to acquire() is given a zero timeout to prevent it from blocking
# because the lock has been obtained by the first call
# In a situation where separate code from the same thread needs to “reacquire” the lock, use
# an RLock instead.