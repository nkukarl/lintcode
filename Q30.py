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