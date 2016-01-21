class Solution:
	def simplifyPath(self, path):
		path = path.split('/')
		stack = []
		for p in path:
			if p == '..':
				if stack:
					stack.pop()
			elif p == '.' or p == '':
				continue
			else:
				stack.append(p)
			# print(stack)
		return '/' + '/'.join(stack)

paths = ['/home/', '/a/./b/../../c/', '/home//foo/']

inst = Solution()
for path in paths:
	print(path, inst.simplifyPath(path))