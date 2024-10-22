class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This solution uses two-pointer approach to swap zero and non-zero elements
        l = r = 0

        while r < len(nums):
            if nums[l] != 0 and l == r:
                r += 1
                l += 1
            
            elif nums[l] == 0 and nums[r] != 0:
                # swap
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            else:
                r += 1