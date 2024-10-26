from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Uses the sliding window technique
        l = 0
        max_len = 0
        counter = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] += 1
            window_len = r - l + 1
            most_freq_char_count = max(list(counter.values()))
            char_replacements = window_len - most_freq_char_count
            
            # The sliding window is invalid when the number of char replacements in the window
            # is greater than the replacements allowed (k)
            while char_replacements > k:
                counter[s[l]] -= 1
                l += 1
                window_len = r - l + 1
                most_freq_char_count = max(list(counter.values()))
                char_replacements = window_len - most_freq_char_count
            
            max_len = max(max_len, window_len)
        return max_len