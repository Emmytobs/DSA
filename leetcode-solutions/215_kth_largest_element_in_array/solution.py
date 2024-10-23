import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        klargest = heapq.nlargest(k, nums)
        return klargest[-1]