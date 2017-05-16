class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums=sorted(nums)
        medium=nums[n/2]
        sum=0
        for i in range(n):
            sum+=abs(nums[i]-medium)
        return sum
