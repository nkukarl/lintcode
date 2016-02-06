'''
Thoughts:

Binary search and insert
Initialise tmp to [] and iterate the items in nums to binary search and insert to tmp
Append the middle item of tmp to res
Return res

'''
class Solution:
    def medianII(self, nums):
        tmp = []
        res = []
        
        for n in nums:
            self.binarySearchInsert(tmp, n)
            res.append(tmp[(len(tmp) - 1) // 2])
            
        return res
        
    def binarySearchInsert(self, nums, n):
        if not nums:
            nums.append(n)
            return
        
        if n >= nums[-1]:
            nums.append(n)
            return
        
        if n <= nums[0]:
            nums.insert(0, n)
            return
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < n:
                left = mid + 1
            else:
                right = mid
        
        nums.insert(left, n)
        

# nums = [4, 5, 1, 3, 2, 6, 0]
nums = [1, 2, 3, 4, 5]
nums = [2, 100, 20]

inst = Solution()
print(inst.medianII(nums))
