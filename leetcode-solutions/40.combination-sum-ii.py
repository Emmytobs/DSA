#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        # Sorting the candidates array is a way to prune the recursive tree (See editorial for more info)
        candidates.sort()
        def backtrack(combination: List[int], curr_target: int, curr_index: int,):
            if curr_target == 0:
                output.append([*combination])

            for i in range(curr_index, len(candidates)):
                candidate = candidates[i]
                # To prevent duplicate solutions, only use distinct candidate numbers
                # for each subproblem at each curr_index
                if(i > curr_index and candidate == candidates[i-1]):
                    continue
                if candidate <= curr_target:
                    combination.append(candidate)
                    backtrack(combination, curr_target - candidate, i + 1) # increment by 1 since we can't repeat candidate numbers
                    combination.pop()

        backtrack([], target, 0)
        return output
# @lc code=end

