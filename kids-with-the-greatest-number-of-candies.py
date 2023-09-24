class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l=[]
        for i in candies:
            if((i+extraCandies)>=max(candies)):
                l.append(True)
            else:
                l.append(False)
        return l
