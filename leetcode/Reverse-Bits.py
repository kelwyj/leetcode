class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans=0
        for i in xrange(32):
            ans =ans<< 1
            ans=ans|((n>>i)&1)
        return ans
