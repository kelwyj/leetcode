class Solution(object):
    def getSum(self, a, b):
        MAX_INT=0X7FFFFFFF
        MIN_INT=0X80000000
        MASK=0X100000000
        while b!=0:
            a,b=(a^b)%MASK,((a&b)<<1)%MASK
        if a<=MAX_INT:
            return a
        else:
            return ~((a%MIN_INT)^MAX_INT)
leetcode
