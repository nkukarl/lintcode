'''
Thoughts:

Initialise prev to None
Store previous character and compare prev with cur
If prev >= cur, add prev to result and update prev to cur
If prev < cur, prev + cur would form a valid two roman letter integer, add this to res and reset prev to None
After exiting the iteration, if prev != None, add prev to res

'''

Int2Roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100:'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
keys, values = [], []
for k, v in Int2Roman.items():
	keys.append(k)
	values.append(v)
Roman2Int = dict(zip(values, keys))

Roman2Int = {'XL': 40, 'L': 50, 'X': 10, 'M': 1000, 'D': 500, 'CD': 400, 'IX': 9, 'IV': 4, 'C': 100, 'I': 1, 'CM': 900, 'XC': 90, 'V': 5}

class Solution:
	def romanToInt(self, s):
		res = 0
		charPrev = ''
		for char in s:
			if not charPrev:
				charPrev = char
			elif Roman2Int[charPrev] >= Roman2Int[char]:
				res += Roman2Int[charPrev]
				charPrev = char
			else:
				res += Roman2Int[charPrev + char]
				charPrev = ''
		if charPrev:
			res += Roman2Int[charPrev]
		return res

inst = Solution()

strings = ['IV', 'XII', 'XXI', 'XCIX']
for s in strings:
	print(inst.romanToInt(s))