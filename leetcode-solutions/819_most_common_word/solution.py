import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'\W+', paragraph.lower()) # splits at all non-alphabetic characters
        word_counter = {}

        for word in words:
            word = word.lower()
            word_counter[word] = 1 + word_counter.get(word, 0)
        
        items = list(word_counter.items())
        most_common = None

        for word, freq in items:
            if word in banned or word == '': continue
            elif most_common is None or freq > most_common[1]:
                most_common = [word, freq]
        
        return most_common[0]
                
