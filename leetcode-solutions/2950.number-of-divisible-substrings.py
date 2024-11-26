#
# @lc app=leetcode id=2950 lang=python3
#
# [2950] Number of Divisible Substrings
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        mapped_digits = [((ord(char) - ord('c')) // 3) + 2 for char in word]
        output = 0
        for num in range(1, 10): # 1 - 9 mapped digits
            sum_prefix = 0
            count = defaultdict(int)
            count[0] = 1
            for i, digit in enumerate(mapped_digits):
                sum_prefix += (digit - num)
                output += count[sum_prefix]
                count[sum_prefix] += 1
        return output
# @lc code=end

