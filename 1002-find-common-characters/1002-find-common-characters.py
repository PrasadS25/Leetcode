class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_count = [0]*26
        for c in words[0]:
            total_count[ord(c)-ord('a')] += 1

        for word in words:
            word_count = [0]*26
            for c in word:
                word_count[ord(c)-ord('a')] += 1
            for i in range(len(total_count)):
                total_count[i] = min(total_count[i],word_count[i])

        res = []
        for i,n in enumerate(total_count):
            if n>0:
                res.extend([chr(i+ord('a'))]*n)
        return res