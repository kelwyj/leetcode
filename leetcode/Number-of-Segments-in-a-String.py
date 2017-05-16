class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s ==None:
            return 0
        else:
            return len(s.split())

 
