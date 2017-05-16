class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        Vow=('a','e','i','o','u','A','E','I','O','U')
        left=0
        right=len(s)-1
        s=list(s)
        while True:
            while left<len(s) and s[left] not in Vow:
                left+=1
            while right>=0 and s[right] not in Vow:
                right-=1
            if left>right:
                break
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)
