class Solution:
	def maxArea(self, heights):
		left, right = 0, len(heights) - 1
		maxArea = 0
		while left < right:
			h = min(heights[left], heights[right])
			maxArea = max(maxArea, (right - left) * h)
			if heights[left] < heights[right]:
				left += 1
			elif heights[left] > heights[right]:
				right -= 1
			else:
				left += 1
				right -= 1
		return maxArea

heights = [1, 3, 2, 4]

inst = Solution()
print(inst.maxArea(heights))