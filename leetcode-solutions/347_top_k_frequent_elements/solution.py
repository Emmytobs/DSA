import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        output = []

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for num, freq in counter.items():
            heapq.heappush(heap, (-1 * freq, num))

        while len(output) < k:
            output.append(heapq.heappop(heap)[1])

        return output
