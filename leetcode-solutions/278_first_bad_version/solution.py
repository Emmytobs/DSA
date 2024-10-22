# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            """
            If using "while l < r", to get the first bad version:
                1) when the element at the mid-point satisfies the condition, 
                move the r pointer to the mid-point (r = m).
                2) Else, move the l pointer to the mid-point + 1 (l = m + 1).

            Another way to implement this is:
            if isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m # assumes m is the first element that satisfies the condition
                r = m - 1
            else:
                l = m + 1
            """
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l # gives the first element in the array that satisfies the condition