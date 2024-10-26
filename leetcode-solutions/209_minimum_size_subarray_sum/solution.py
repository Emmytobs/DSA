from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Refactored implementation 
        min_len = float("inf")
        l = curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len

        # Original implementation
        # if len(nums) == 1: 
        #     return 1 if nums[0] >= target else 0

        # l, r = 0, 0
        # min_len = inf
        # curr_sum = nums[l]
        # curr_len = 1
        # while l < len(nums):
        #     while curr_sum < target and r < len(nums) - 1:
        #         r += 1
        #         curr_sum += nums[r]
        #         curr_len += 1
        #     if r == len(nums)-1 and l == 0 and curr_sum < target:
        #         return 0
        #     if curr_sum >= target:
        #         min_len = min(curr_len, min_len)
        #         curr_sum -= nums[l]
        #         curr_len -= 1
        #     l += 1
        
        # return min_len

