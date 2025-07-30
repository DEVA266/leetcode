# Last updated: 7/30/2025, 12:23:38 PM
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        sorted_words = sorted(word_count.keys(),key = lambda w : (-word_count[w],w))
        return sorted_words[:k]

        


        