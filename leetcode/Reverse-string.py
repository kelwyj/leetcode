"""
Write function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        #solution 2
        return "".join(reversed(s)
