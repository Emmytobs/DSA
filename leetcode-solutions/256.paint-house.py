class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        output = float('inf')
        memo = dict()
        for i, cost in enumerate(costs[0]):
            output = min(output, self._minCost(costs, cost, 0, i, memo))
        return output

    def _minCost(self, costs: List[List[int]], cost: int, house_i: int, cost_i: int, memo) -> int:
        memo_key = (cost, house_i, cost_i)
        # Base case
        if house_i == len(costs) - 1:
            return cost

        # Memoization step
        if memo_key in memo:
            return memo[memo_key]

        next_house_costs = costs[house_i + 1]
        min_cost_result = float('inf')
        for i in range(len(next_house_costs)):
            next_house_cost = next_house_costs[i]
            next_house_i = house_i + 1
            if i != cost_i:
                min_cost_result = min(min_cost_result, cost + self._minCost(costs, next_house_cost, next_house_i, i, memo))
        memo[memo_key] = min_cost_result
        return min_cost_result