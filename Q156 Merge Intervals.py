'''
Thoughts:

Sort intervals based on the start time of each interval
Iterate the intervals, if the start time of current interval is smaller than or equal to the end time of previous interval, update the end time of previous interval to the max of the end time of the previous and current interval
Else, append current interval to res

'''

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

class Solution:
	def merge(self, intervals):
		if not intervals:
			return []
		intervals.sort(key = lambda x : x.start)
		res = [intervals[0]]
		for interval in intervals[1:]:
			if interval.start <= res[-1].end:
				res[-1].end = max(interval.end, res[-1].end)
			else:
				res.append(interval)
		return res

			

intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]

inst = Solution()
res = inst.merge(intervals)

for r in res:
	print(r.start, r.end)