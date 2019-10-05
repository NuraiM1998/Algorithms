class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        req_sum = len(nums)*(len(nums)+1)/2
        act_sum = sum(nums)
        return req_sum-act_sum