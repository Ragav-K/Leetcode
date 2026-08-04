class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > (sum(nums[i+1:]))/(len(nums)-i-1):
                count += 1
        return count