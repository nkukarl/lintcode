'''
Thoughts:

Use two pointers, left and right
Calculating the current rectangle area by using the difference of right and left and the smaller of height right and height left
If left height < right height, left plus 1
If right height < left height, right minus 1
If left height == right height, left plus 1 and right minus 1

'''

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