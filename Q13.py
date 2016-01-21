class Solution:
	def strStr(self, source, target):
		if target == '':
			return 0
		if not target:
			return -1
		if not source:
			return -1
		tmp = source.split(target)
		pos = len(tmp[0])

		if pos == len(source):
			return -1
		return pos

source = 'source'
target = 'target'

source = 'abcdabhcdefg'
target = 'h'

inst = Solution()
print(inst.strStr(source, target))
