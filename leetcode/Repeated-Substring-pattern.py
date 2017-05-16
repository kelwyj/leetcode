class Solution(object):
    def repeatedSubstringPattern(self, str):
        if not str:
            return False
        ss = (str + str)[1:-1]
        return ss.find(str) != -1       
        """
        :type str: str
        :rtype: bool
        """
        """
        n=len(str)
        solution 1:
        if n<2 :
            return False
        for i in range(1,n):
            if str[i:]+str[:i]==str:
                return True
        return False
        """
        """solution 2
        n=len(str)
        div=n/2
        while div>0:
            if str[0:div]*(n/div)==str:
                return True
            div-=1
        return False
        """
        """solution 3

        
leetcode
