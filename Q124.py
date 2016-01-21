class Solution:
	def longestConsecutive(self, nums):
		nums = list(set(nums))
		tmp = dict()
		for n in nums:
			tmp[n] = (0, 0)
		for k in tmp.keys():
			left, right = -1, -1
			if k - 1 in tmp.keys():
				left1, right1 = tmp[k - 1]
				tmp[k - 1] = (left1, right1 + 1)
				left = left1
			if k + 1 in tmp.keys():
				left2, right2 = tmp[k + 1]
				tmp[k + 1] = (left2 + 1, right2)
				right = right2
			tmp[k] = (left + 1, right + 1)
		print(tmp)
		# return max(tmp.values())

nums = [100, 4, 200, 1, 3, 2, 5, 7, 9, 6, 8]
# nums = [100, 4, 200, 1, 3, 2, 1]
# nums = [-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1]

print(sorted(list(set(nums))))

inst = Solution()
print(inst.longestConsecutive(nums))