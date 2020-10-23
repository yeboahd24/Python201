#!usr/bin/env/python3

"""Consider @property instead of refactoring attribute
	Eg: implementation of leaky bucket quota
"""

from datetime import datetime, timedelta

class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return f'Bucket(quota={self.quota})'

	def fill(self, bucket, amount):
		now = datetime.now()
		if(now - bucket.reset_time) > bucket.period_delta:
			bucket.quota = 0
			bucket.reset_time = now
		bucket.quota += amount

	def deduct(self, bucket, amount):
		now = datetime.now()
		if(now - bucket.reset_time) > bucket.period_delta:
			return False # Bucket hasn't be filled this periode
		if bucket.quota - amount < 0:
			return False # Bucket was filled but not enough
		bucket.quota -= amount
		return True # Bucket had enough, quota consume


# bucket = Bucket(60)
# bucket.fill(bucket, 100)
# print(bucket)

class NewBucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.max_quota = 0
		self.quota_consumed = 0
		self.reset_time = datetime.now()

	def __repr__(self):
		return (f'NewBucket(max_quota={self.max_quota}, ' f'quota_consumed={self.quota_consumed})')

	@property
	def quota(self):
		return self.max_quota - self.quota_consumed

	@quota.setter
	def quota(self, amount):
		delta = self.max_quota - amount
		if amount == 0:
			self.quota_consumed = 0 # Quota being reset for new period
			self.max_quota = 0
		elif delta < 0:
			assert self.quota_consumed == 0 # Quota being filled for new period 
			self.max_quota = amount
		else:
			assert self.max_quota >= self.quota_consumed
			self.quota_consumed += delta # Quota being consumed during the period

	def fill(self, bucket, amount):
		now = datetime.now()
		if(now - bucket.reset_time) > bucket.period_delta:
			bucket.quota = 0
			bucket.reset_time = now
		bucket.quota += amount

	def deduct(self, bucket, amount):
		now = datetime.now()
		if(now - bucket.reset_time) > bucket.period_delta:
			return False # Bucket hasn't be filled this periode
		if bucket.quota - amount < 0:
			return False # Bucket was filled but not enough
		bucket.quota -= amount
		return True # Bucket had enough, quota consume



bucket = NewBucket(60)
print('Initial', bucket)
bucket.fill(bucket, 100)
print('Filled', bucket)
bucket.deduct(bucket, 40)
print('Deduct', bucket)