class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position = self.binary_search(nums, target, True)
        second_position = self.binary_search(nums, target, False)

        return [first_position, second_position]
        
    def binary_search(self, nums: List[int], target: int, first_position: bool):
        l, r = 0, len(nums) - 1
        position = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                # After finding an element that equals the target
                position = mid
                if first_position:
                    # to find the first position of the element, repeat binary search on the first half 
                    r = mid - 1
                else:
                    # to find the last position of the element, repeat binary search on the second half
                    l = mid + 1
        return position