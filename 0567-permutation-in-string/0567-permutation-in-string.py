class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = [0]*26
        hash2 = [0]*26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            hash1[ord(s1[i])-ord('a')] += 1
            hash2[ord(s2[i])-ord('a')] += 1

        i = 0 
        for j in range(len(s1),len(s2)):

            if hash1 == hash2:
                return True
            ind = ord(s2[j]) - ord('a')
            hash2[ind] += 1
            hash2[ord(s2[i]) - ord('a')] -= 1
            i+=1

        return hash1 == hash2