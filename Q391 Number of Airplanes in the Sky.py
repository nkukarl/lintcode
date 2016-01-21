'''
Thoughts:

Solution 1 is trivial
According to the question description
"if landing and flying happens at the same time, we consider landing should happen at first"
Hence, the landing time has been deducted by 0.5
1st pass to store all the flying and landing time spots
Sort the time spots together, since landing time is always X.5, we can tell the difference between flying and landing
2nd pass to record the maximum number of planes in the sky (MAX), current number (cur) plus 1 when meeting an integer, current number minus 1 when meeting a X.5 number
Keep updating MAX by comparing MAX with cur

'''

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

# class Solution:
# 	def countOfAirplanes(self, airplanes):
# 		if not airplanes:
# 			return 0
# 		start = airplanes[0].start
# 		end = airplanes[0].end

# 		for a in airplanes[1:]:
# 			start = min(a.start, start)
# 			end = max(a.end, end)

# 		summary = dict()

# 		for a in airplanes:
# 			for t in range(a.start, a.end):
# 				summary[t] = summary.get(t, 0) + 1

# 		return max(summary.values())

# airplanes = [Interval(1, 10), Interval(2, 3), Interval(5, 8), Interval(4, 7)]
# airplanes = []

# inst = Solution()
# print(inst.countOfAirplanes(airplanes))

class Solution_opt:
	def countOfAirplanes(self, airplanes):
		if not airplanes:
			return 0
		summary = []
		for a in airplanes:
			summary.append(a.start)
			summary.append(a.end - 0.5)
		summary.sort()
		MAX = 0
		counter = 0
		for time in summary:
			if time % 1 == 0:
				counter += 1
			else:
				counter -= 1
			MAX = max(MAX, counter)
		return MAX


airplanes = [Interval(1, 10), Interval(2, 3), Interval(5, 8), Interval(4, 7)]
airplanes = [Interval(1, 10), Interval(2, 3), Interval(5, 8), Interval(4, 7)]

inst = Solution_opt()
print(inst.countOfAirplanes(airplanes))