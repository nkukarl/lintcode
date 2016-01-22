'''
Thoughts:

Two level iterations
Summarise the statistics using summary dictionary
Initialised dictionary with points with inf slope equal to 0 and duplicated points equal to 1 (itself)
If two points have same x and y, duplicated points number plus 1
If only two xs are equal, points with inf slope plus 1
Update max points by comparing res with max(summary.values()) + dupPts in the outer level iterations

'''

class Point:
	def __init__(self, a = 0, b = 0):
		self.x, self.y = a, b

class Solution:
	def maxPoints(self, points):
		if len(points) < 3:
			return len(points)

		res = 1

		for p1 in points:
			dupPts = 1
			summary = {'inf': 0}
			for p2 in points:
				if p1 != p2:
					x1, y1 = p1.x, p1.y
					x2, y2 = p2.x, p2.y
					if x1 == x2 and y1 == y2:
						dupPts += 1
					elif x1 == x2:
						summary['inf'] += 1
					else:
						slope = 1.0 * (y1 - y2) / (x1 - x2)
						summary[slope] = summary.get(slope, 0) + 1
			res = max(max(summary.values()) + dupPts, res)

		return res