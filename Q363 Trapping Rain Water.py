'''
Thoughts:

Find the highest boundary at the left and right of each position
The boundary is determined by the smaller one of left and right boundary
For each position, if the boundary is greater than the height of current position, area will be 0
Else, area will be the difference between boundary and current position height

When implementing the algorithm
Insert and append 0 to the beginning and the end of heights
Left boundary is equal to the maximum of maximum boundary found and the height of the adjacent position
For the right boundary, reverse heights and perform the same computation
Remember to reverse both heights and right before calculating the area
Also remember to remove the 0s at the beginning and the end of heights

'''


class Solution:
	def trapRainWater(self, heights):
		left = [0]
		right = [0]
		
		heights = [0] + heights + [0]
		for i in range(1, len(heights)):
			left.append(max(left[-1], heights[i - 1]))
		left.pop(0)
		
		heights.reverse()
		for i in range(1, len(heights) - 1):
			right.append(max(right[-1], heights[i - 1]))
		right.pop(0)
		
		right.reverse()

		heights.reverse()
		heights.pop(0)
		heights.pop()
		
		area = 0
		
		for i in range(len(heights)):
			h = heights[i]
			b = min(left[i], right[i])
			area += max(b - h, 0)
			
		return area

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

inst = Solution()
print(inst.trapRainWater(heights))