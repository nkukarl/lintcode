'''
Thoughts:

Append the new interval to intervals and then sort intervals based on the start of each interval
Initialise res to [intervals[0]]
Iterate the intervals, if the start of current interval is smaller than or equal to the end of the last interval of res, update the end of the last interval to the larger one of the end of the last interval of res and the end of the current interval
If the start of current interval is greater than the end of the last interval, append the current interval of res

Return res

'''

class Interval:
	def __init__(self, start, end):
		self.start, self.end = start, end

class Solution:
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)

		intervals.sort(key = lambda x : x.start)

		res = [intervals[0]]

		for i in intervals[1:]:
			if i.start <= res[-1].end:
				res[-1].end = max(i.end, res[-1].end)
			else:
				res.append(i)
		return res

intervals = [Interval(1, 2), Interval(5, 9)]
# newInterval = Interval(2, 5)
newInterval = Interval(3, 4)

inst = Solution()
res = inst.insert(intervals, newInterval)
for i in res:
	print(i.start, i.end)