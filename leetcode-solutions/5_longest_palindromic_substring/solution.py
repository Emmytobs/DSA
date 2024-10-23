class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        
        for i in range(len(s)):
            odd = self.expand_from_center(s, i, i)
            # Since even-length strings have no center to expand from, we set the right pointer next to the left
            even = self.expand_from_center(s, i, i + 1)

            if len(odd) > len(longest_palindrome):
                longest_palindrome = odd
            if len(even) > len(longest_palindrome):
                longest_palindrome = even
        
        return longest_palindrome
    
    def expand_from_center(self, s, l, r):
        """
            This method uses the two-pointer approach. 
            However, instead of comparing characters starting with those farthest apart (expanding inwards),
            it starts with those closest to each other (thus, it expands outward from the center)
        """
        palindrome = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindrome = s[l:r + 1]
            l -= 1
            r += 1
        
        return palindrome