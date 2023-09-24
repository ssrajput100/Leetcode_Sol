class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        e=len(str2)
        l=""
        for i in range(e):
            q=str2[:e-i]
            if (len(str1)%len(q)==0) and (len(str2)%len(q)==0) and q in str1:
                r=int(len(str1)/len(q))
                p=int(len(str2)/len(q))
                if (str1==(q*r) and str2==(q*p)):
                    return q
        return l
