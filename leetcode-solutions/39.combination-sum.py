#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        BASE_CASE = 0
        output = []
        def backtrack(temp_list: List[int], curr_target: int, start) -> int:
            if curr_target == BASE_CASE:
                output.append([*temp_list])
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate <= curr_target:
                    temp_list.append(candidate)
                    # The code above the recursive call runs when traversing down the recursive tree

                    """
                        In order to avoid duplicate solutions,
                        we explore subproblems starting from the index, i, of the parent function call
                    """
                    backtrack(temp_list, curr_target - candidate, i)

                    # The code below the recursive call runs when backtracking
                    temp_list.pop()

        backtrack([], target, 0)
        return output
# @lc code=end

