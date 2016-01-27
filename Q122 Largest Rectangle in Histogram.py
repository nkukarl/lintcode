'''
Thoughts:

Append 0 to height to force popping out stack at the end
Initialise stack with [-1]

Iterate all the elements in height
If height is greater than or equal to height[stack[-1]], append the index of element to stack
Else, popping out the last element of stack, calculate the size the rectangle, update the maximum size, until height is greater than or equal to height[stack[-1]]
When calculating the size of the rectangle, the length of the rectangle is height[stack.pop()], the width of the rectangle is the difference between current element index and the index at the current stack top, don't forget to minus 1

'''

class Solution:
	def largestRectangleArea(self, height):
		stack = [-1]
		maxArea = 0
		height += [0]
		for i in range(len(height)):
			h = height[i]
			if stack == [-1]:
				stack.append(i)
			else:
				if h < height[stack[-1]]:
					while len(stack) > 1 and h < height[stack[-1]]:
						tmp = stack.pop()
						area = height[tmp] * (i - stack[-1] - 1)
						maxArea = max(maxArea, area)
					stack.append(i)
				else:
					stack.append(i)
		return maxArea

class Solution_opt:
	def largestRectangleArea(self, height):
		stack = [-1]
		maxArea = 0
		height += [0]
		for i in range(len(height)):
			h = height[i]
			if h >= height[stack[-1]]:
				stack.append(i)
			else:
				while stack and h < height[stack[-1]]:
					tmp = stack.pop()
					area = height[tmp] * (i - stack[-1] - 1)
					maxArea = max(maxArea, area)
				stack.append(i)
		return maxArea

	def largestRectangleArea_concise(self, height):
		stack = [-1]
		maxArea = 0
		height += [0]
		for i in range(len(height)):
			h = height[i]
			if h < height[stack[-1]]:
				while stack and h < height[stack[-1]]:
					tmp = stack.pop()
					maxArea = max(maxArea, height[tmp] * (i - stack[-1] - 1))
			stack.append(i)
		return maxArea

height = [2, 1, 5, 6, 2, 3]
height = [1, 1, 1]
height = [1, 2, 4, 3]
height = [1, 2, 3, 4]
height = [1, 2, 1, 2, 1, 10]
height = [5, 4, 1, 2]

inst = Solution_opt()
print(inst.largestRectangleArea_concise(height))