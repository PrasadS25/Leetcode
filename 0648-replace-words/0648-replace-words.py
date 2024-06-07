class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_arry = sentence.split()
        hash_set = set(dictionary)

        def shortest_root(word):

            for i in range(len(word)):
                if word[0:i] in hash_set:
                    return word[0:i]
            return word
        for word in range(len(word_arry)):
            word_arry[word] = shortest_root(word_arry[word])
        
        return " ".join(word_arry)
