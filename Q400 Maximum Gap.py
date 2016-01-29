'''
Thoughts:

The tricky part is the bucketRange and bucketNumber
For an array with m elements, if the minimum and maximum elements are A and B,
the maximum gap is equal to or greater than (B - A) / (m - 1) [ceil]

(B - A) / (m - 1) [ceil] can be obtained using either math.ceil((B - A) / (m - 1))
or using (B - A - 1) // (m - 1) + 1, this will avoid adding 1 when (B - A) % (m - 1) == 0

bucketNumber is then calculated as (B - A) // bucketRange + 1

Initialise buckets to [None] * bucketNumber

Iterate all the numbers in nums, for a certain number n, locate its bucket using loc = (n - A) // bucketRange
If buckets[loc] is None, change it to {'min': n, 'max': n}
Otherwise, update buckets[loc]['min'] and buckets[loc]['max'] by comparing their original values to n

Initialise maxGap to 0
Iterate all the buckets, ignore empty buckets[i]
Otherwise, search for the next non-empty buckets[j]
Update maxGap by comparing its original value to buckets[j]['min'] - buckets[i]['max']
Update i to j since the empty buckets in between can be ignored

Return maxGap

'''

class Solution:
	def maximumGap(self, nums):
		m = len(nums)
		if m < 2:
			return 0
		A, B = min(nums), max(nums)
		bucketRange = max(1, (B - A - 1) // (m - 1) + 1)
		bucketNumber = (B - A) // bucketRange + 1
		buckets = [None] * m
		for n in nums:
			loc = (n - A) // bucketRange
			bucket = buckets[loc]
			if not bucket:
				bucket = {'min': n, 'max': n}
				buckets[loc] = bucket
			else:
				buckets[loc]['min'] = min(buckets[loc]['min'], n)
				buckets[loc]['max'] = max(buckets[loc]['max'], n)

		maxGap = 0
		for i in range(bucketNumber):
			if not buckets[i]:
				continue
			j = i + 1
			while j < bucketNumber and not buckets[j]:
				j += 1
			if j < bucketNumber:
				maxGap = max(maxGap, buckets[j]['min'] - buckets[i]['max'])
			i = j

		return maxGap