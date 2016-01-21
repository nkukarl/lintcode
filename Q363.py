class Solution:
	def trapRainWater(self, heights):
		left, right = [0], [0]
		area = 0
		for i in range(len(heights)):
			h = heights[i]
			left.append(max(h, left[-1]))
		for i in range(len(heights) - 1, -1, -1):
			h = heights[i]
			right.append(max((h), right[-1]))
		right = right[::-1]
		for i in range(len(heights)):
			h = heights[i]
			b = min(left[i], right[i])
			# print(h, left[i], right[i], max(b - h, 0))
			area += max(b - h, 0)
		return area	

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

inst = Solution()
print(inst.trapRainWater(heights))