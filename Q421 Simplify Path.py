'''
Thoughts:

Stack
Split the path using '/'
Iterate the path,
pop out the top element from stack if meets '..'
do nothing if meets '.' or empty string
push others to the stack
return '/' plus the elements in the stack joined together

'''

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