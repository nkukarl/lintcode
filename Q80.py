import random
class Solution:
	def median(self, nums):
		if len(nums) % 2 == 0:
			return self.helper(nums, len(nums) // 2)
		return self.helper(nums, len(nums) // 2 + 1)

	def helper(self, nums, k):
		pivot = random.choice(nums)
		nums1, nums2 = [], []
		for n in nums:
			if n < pivot:
				nums1.append(n)
			else:
				nums2.append(n)
		if len(set(nums1 + nums2)) == 1:
			return pivot
		if len(nums1) == k - 1:
			return pivot
		if len(nums1) > k - 1:
			return self.helper(nums1, k)
		return self.helper(nums2, k - len(nums1))

nums = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(nums)

nums = [-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]

inst = Solution()
print(inst.median(nums))