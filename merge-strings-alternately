class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        d=''
        if (len(word1)>=len(word2)):
            for i in range(len(word2)):
                d+=word1[i]
                d+=word2[i]
            for j in range(len(word2),len(word1)):
                d+=word1[j]
        else:
            for i in range(len(word1)):
                d+=word1[i]
                d+=word2[i]
            for j in range(len(word1),len(word2)):
                d+=word2[j]
        return d
           
