from math import ceil

"""
This is a very interesting application of Binary Search!

> Brute force approach:

To determine the minimum number of bananas to eat per hour such that all the bananas will be eaten within the given time, we can try eating 1 banana, then 2, then 3, then 4... until we find the number of bananas that satisfies the constraint of eating all bananas in all piles. This approach is a linear search, which we can convert to a binary search!

> Optimized approach using Binary Search:

Let's say the maximum bananas across all piles is X. Then eating X bananas every hour will guarantee that we will eat all the bananas in all piles, which have at most X bananas in them. Thus, the minimum number of bananas will be in the set of numbers between 1 and X, inclusive ([1, X]).

We can apply binary search over this set of number to find the first number that satisfies the constraint.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num_of_bananas_in_pile = max(piles)

        l, r = 1, max_num_of_bananas_in_pile

        while l <= r:
            m = (l + r) // 2
            if self.can_finish_bananas(piles, m, h):
                r = m - 1
            else:
                l = m + 1
        return l
        
    def can_finish_bananas(self, piles, hourly_eating_speed, h) -> bool:
        total_eating_hours = 0
        for pile in piles:
            total_eating_hours += ceil(pile / hourly_eating_speed)
            if total_eating_hours > h:
                return False
        return True
            
