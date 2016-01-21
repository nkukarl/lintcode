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