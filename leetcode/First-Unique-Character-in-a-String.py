"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #solution 1
        return min([s.find(i) for i in 'abcdefghijklmnopqrstuvwxyz' if s.count(i)==1] or [-1])
    
        #solution 2        
        ant={}
        for c in s:
            if c in ant:
                ant[c]=ant[c]+1
            else:
                ant[c]=1
        for i in range(0,len(s)):
            x=s[i]
            if ant[x]==1:
                return i
        return -1
