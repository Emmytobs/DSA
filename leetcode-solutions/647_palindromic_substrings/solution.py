# This problem is very similar to #5: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            # Returns the palindromes for odd-length substrings
            count_for_odd = self.count_palindromes(s, i, i)
            # Returns the palindromes for even-length substrings
            count_for_even = self.count_palindromes(s, i, i + 1)
            output += (count_for_odd + count_for_even)
        return output
    
    def count_palindromes(self, s, l, r):
        """
            Uses two-pointer technique, expanding from the center
        """
        no_of_palindromes = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            no_of_palindromes += 1
            l -= 1
            r += 1
        return no_of_palindromes