class Solution:
	def canCompleteCircuit(self, gas, cost):
		totalGas = sum(gas)
		if totalGas < sum(cost):
			return -1
		curGas = totalGas
		minGas = totalGas
		stationNo = 0
		for i in range(1, len(gas)):
			curGas = curGas - cost[i - 1] + gas[i - 1]
			if curGas < minGas:
				minGas = curGas
				stationNo = i
		curGas = curGas - cost[-1] + gas[-1]
		if curGas < minGas:
			stationNo = 0
		return stationNo

gas = [1, 2, 3, 3]
cost = [2, 1, 5, 1]

inst = Solution()
print(inst.canCompleteCircuit(gas, cost))