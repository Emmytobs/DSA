#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Progamming
        def _numDecodings(s: str, i: int, memo: Dict[int, int]) -> int:
            n = len(s)
            # Two base cases
            if i == n:
                return 1
            if s[i] == '0':
                return 0 # sub string starting with 0 is not a valid encoding
            # Use memoized value
            if i in memo:
                return memo[i]
            res = _numDecodings(s, i + 1, memo)
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += _numDecodings(s, i + 2, memo)
            memo[i] = res
            return memo[i]
        return 0 if len(s) == 0 else _numDecodings(s, 0, {})
# @lc code=end

