class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i=len(g)-1
        j=len(s)-1
        g=sorted(g)
        s=sorted(s)
        result=0
        if j<0:
            return 0
        while (i>=0)&(j>=0):
            if g[i]<=s[j]:
                result+=1
                j-=1
            i-=1
        return result
leetcode
