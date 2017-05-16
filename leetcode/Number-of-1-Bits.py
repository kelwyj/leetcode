class Solution(object):
    def hammingWeight(self, n):
        ans=0
        for i in xrange(32):
            if (n>>i)&1==1:
                ans+=1
        return ans
        """
        :type n: int
        :rtype: int
        another  solution :
        s=bin(n)
        result=0
        for x in s:
            if x =='1':
                result+=1
        return result
        """
